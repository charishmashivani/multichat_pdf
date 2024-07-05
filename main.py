import streamlit as st
import numpy as np
from numpy.linalg import norm
import fitz  # PyMuPDF
import pandas as pd
import openai
from langchain.text_splitter import RecursiveCharacterTextSplitter

openai.api_key = ''

def get_embedding(text, model="text-embedding-ada-002"):
    text = text.replace("\n", " ")
    return openai.Embedding.create(input=[text], model=model)['data'][0]['embedding']

def extract(pdf_path, users_question):
    # Open the PDF file
    document = fitz.open(pdf_path)
    # Extract text from each page
    text = ""
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text()

    article_text = text

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=100,
        chunk_overlap=20,
        length_function=len,
    )
    texts = text_splitter.create_documents([article_text])
    text_chunks = [text.page_content for text in texts]

    df = pd.DataFrame({'text_chunks': text_chunks})

    # Get embeddings from text-embedding-ada model
    df['ada_embedding'] = df.text_chunks.apply(lambda x: get_embedding(x, model='text-embedding-ada-002'))

    # Calculate the embeddings for the user's question
    question_embedding = get_embedding(text=users_question, model="text-embedding-ada-002")

    # Create a list to store the calculated cosine similarity
    cos_sim = []
    for index, row in df.iterrows():
        A = row.ada_embedding
        B = question_embedding
        # Calculate the cosine similarity
        cosine = np.dot(A, B) / (norm(A) * norm(B))
        cos_sim.append(cosine)
    df["cos_sim"] = cos_sim
    df = df.sort_values(by=["cos_sim"], ascending=False)

    # Define the context for the prompt by joining the most relevant text chunks
    context = " ".join(df.iloc[0:20]['text_chunks'].tolist())

    # Define the prompt template
    template = """
    You are a chat bot who loves to help people! Given the following context sections, answer the
    question using only the given context. If you are unsure and the answer is not
    explicitly written in the documentation, say "Sorry, I don't know how to help with that."

    Context sections:
    {context}

    Question:
    {users_question}

    Answer:
    """

    # Fill the template with context and user's question
    filled_template = template.format(context=context, users_question=users_question)

    # Create the response using the chat completion endpoint
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": filled_template}
        ],
        max_tokens=150,
        temperature=0.7,
    )

    return response.choices[0]['message']['content'].strip()

# Streamlit UI
st.title("PDF Q&A Bot")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
user_question = st.text_input("Enter your question")

if st.button("Get Answer"):
    if uploaded_file is not None and user_question:
        with open("uploaded_pdf.pdf", "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        answer = extract(pdf_path="uploaded_pdf.pdf", users_question=user_question)
        st.write("Answer:", answer)
    else:
        st.write("Please upload a PDF file and enter a question.")
