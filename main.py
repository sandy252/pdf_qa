from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
import pinecone
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
import os
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

pdf_folder = 'uploaded_pdfs'
if not os.path.exists(pdf_folder):
    os.makedirs(pdf_folder)

# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# PINECONE_ENV = os.getenv("PINECONE_ENV")
# PINECONE_API = os.getenv("PINECONE_API")

OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
PINECONE_ENV = st.secrets["PINECONE_ENV"]
PINECONE_API = st.secrets["PINECONE_API"]

st.title("Ask questions to you PDF")
message = st.empty()
# Upload PDF file
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    # Delete the previous PDF file, if it exists
    for existing_file in os.listdir(pdf_folder):
        os.remove(os.path.join(pdf_folder, existing_file))

    # Save the newly uploaded PDF to the 'uploaded_pdfs'
    with open(os.path.join(pdf_folder, uploaded_file.name), "wb") as f:
        # message.text("Data Loading...Started...✅✅✅")
        f.write(uploaded_file.read())

    loader = PyPDFLoader(os.path.join(pdf_folder, uploaded_file.name))
    message.text("Data Loading...Started...✅✅✅")
    data = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    message.text("Text Splitter...Started...✅✅✅")
    texts = text_splitter.split_documents(data)

    # embeddings = OpenAIEmbeddings(openai_api_key=os.getenv('OPENAI_API_KEY'))
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

    message.text("Embedding Vector Started Building...✅✅✅")

    pinecone.init(
        api_key=PINECONE_API,
        environment=PINECONE_ENV
    )
    index_name = "pdfqa"

    docsearch = Pinecone.from_texts([t.page_content for t in texts], embeddings, index_name=index_name)
    message.text("Embedding Vector Built successfully...✅✅✅")

    query = st.text_input("Enter your question")
    if query:
        # query = "tell me about the waste classification and management system."
        docs = docsearch.similarity_search(query)

        llm = OpenAI(temperature=0.5, openai_api_key=OPENAI_API_KEY)
        chain = load_qa_chain(llm, chain_type="stuff")
        st.write(chain.run(input_documents=docs, question=query))
