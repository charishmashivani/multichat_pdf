# multichat_pdf
VI semester Mini project

Here is a README file for the PDF Q&A Bot project:

---

# PDF Q&A Bot

The PDF Q&A Bot is a Streamlit application that allows users to upload PDF files and ask questions about their content. The application uses OpenAI embeddings to analyze the text in the PDFs and generate relevant answers.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

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

- `numpy`: Fundamental package for scientific computing.
- `langchain`: Library for building language models.
- `pandas`: Data manipulation and analysis library.
- `openai==0.28`: OpenAI Python client library.
- `pymupdf`: Library for reading and manipulating PDF files.

These dependencies are listed in the `requirements.txt` file and can be installed using:
```bash
pip install -r requirements.txt
```

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
