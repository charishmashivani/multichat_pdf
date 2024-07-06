# Multi-Chat PDF Bot

The Multi-Chat PDF Bot is a Streamlit application that allows users to upload PDF files and ask questions about their content. The application uses OpenAI embeddings to analyze the text in the PDFs and generate relevant answers. It processes PDF documents by embedding content and calculating vector distances. It uses Retrieval-Augmented Generation (RAG) techniques with pre-trained LLMs to provide answers based on user prompts.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)

## Features

- **Upload PDF Files**: Users can upload PDF files directly through the web interface.
- **Ask Questions**: Enter questions related to the content of the uploaded PDF and receive accurate answers.
- **Powered by OpenAI**: Utilizes OpenAI embeddings for text analysis and question answering.

## Installation

To install and run the PDF Q&A Bot locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/pdf-qa-bot.git
   cd pdf-qa-bot
   ```

2. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To start the application, run the following command:
```bash
streamlit run main.py
```

### Using the Application

1. **Upload a PDF**: Click on the "Browse files" button to upload a PDF document.
2. **Ask a Question**: Enter your question in the text box provided.
3. **Receive an Answer**: The application will process the PDF and generate an answer based on the content.

## Dependencies

The application relies on the following Python libraries:

- `langchain`: Library for building language models.
- `pandas`: Data manipulation and analysis library.
- `openai==0.28`: OpenAI Python client library.
- `pymupdf`: Library for reading and manipulating PDF files.

These dependencies are listed in the `requirements.txt` file and can be installed using:
```bash
pip install -r requirements.txt
```
