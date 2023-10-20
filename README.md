# PDF QA Bot

PDF QA Bot is a web application built with Streamlit that allows users to upload PDF files and ask questions about the content of the PDF. The application uses the power of Langchain for natural language processing and OpenAI's GPT for answering questions. It also utilizes Pinecone for storing and retrieving embeddings for efficient and accurate question-answering.

## Features

- Upload PDF files for analysis.
- Ask questions about the content of the uploaded PDF.
- Utilizes Langchain for PDF text extraction.
- Employs OpenAI's GPT for answering questions.
- Efficient embeddings storage and retrieval with Pinecone.
## Demo and Screenshot
click [Here](https://drive.google.com/file/d/1JPX9A0UeQyKf267r7RLcYjAY9BzEIP2o/view?usp=sharing) to watch the demo of the web app.

### ScreenShot
![screenshot-1](https://github.com/sandy252/pdf_qa/assets/66490787/1b81a377-1e8f-40fa-99fb-0e9cb675c254)
## Getting Started

### Prerequisites

Make sure you have the following prerequisites installed:

- Python 3.10
- Streamlit
- Langchain
- OpenAI's GPT model
- Pinecone

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/sandy252/pdf_qa.git
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up your API keys and environment variables for Langchain, OpenAI, and Pincone. Ensure your API keys are stored securely in environment variables.

4. Run the Streamlit app:

   ```bash
   streamlit run main.py
   ```

5. Open your web browser and access the app at `http://localhost:8501` or the URL provided by Streamlit.

## Usage

1. Upload a PDF file using the provided file uploader.

2. Ask a question related to the content of the PDF.

3. The app will use Langchain to extract text from the PDF, GPT to answer the question, and Pincone for efficient embeddings storage and retrieval.

4. The answer to your question will be displayed on the app.



## Acknowledgments

- Thanks to Streamlit, Langchain, OpenAI, and Pinecone for their fantastic tools and services.

## Contact

Have questions or suggestions? Feel free to contact us at kashyapsandeep252@gmail.com.
