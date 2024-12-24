import streamlit as st
import os
import PyPDF2
from langchain_community.vectorstores import Chroma
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.chat_models import ChatOllama
from langchain_community.embeddings.ollama import OllamaEmbeddings
from langchain_openai import ChatOpenAI
from langchain.schema import Document
from ingest import initialize_vector_store
import tempfile
from io import BytesIO


# --- Fonction pour lire un fichier PDF ---
def read_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    all_page_text = ""
    for page in pdf_reader.pages:
        text = page.extract_text()
        if text:  # Vérifie si le texte est non vide
            all_page_text += text + "\n"
    return all_page_text if all_page_text else "Le document PDF est vide ou non lisible."


# --- Fonction pour traiter une question avec un document ---
def analyze_document_with_question(doc, question):
    model = ChatOllama(model="mistral")
    document = Document(page_content=doc)
    text_splitter = CharacterTextSplitter.from_tiktoken_encoder(chunk_size=800, chunk_overlap=0)
    doc_splits = text_splitter.split_documents([document])

    vectorstore = Chroma.from_documents(
        documents=doc_splits,
        collection_name="rag-chroma",
        embedding=OllamaEmbeddings(model="mxbai-embed-large:latest"),
    )
    retriever = vectorstore.as_retriever(k=2)

    after_rag_template = """Answer the question based only on the following context:
    {context}
    Question: {question}
    """
    after_rag_prompt = ChatPromptTemplate.from_template(after_rag_template)

    after_rag_chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | after_rag_prompt
        | model
        | StrOutputParser()
    )

    return after_rag_chain.invoke(question)


# --- Interface utilisateur avec Streamlit ---
st.title("Pulse Life 🫀 - Analyse de documents médicaux")
st.write("Téléchargez un document médical pour poser des questions ou obtenir un résumé.")

# --- Gestion de l'upload de fichiers ---
uploaded_file = st.file_uploader("Téléchargez un fichier (PDF uniquement)", type=["pdf"])

if uploaded_file:
    # Lecture et affichage du document PDF
    with st.spinner("Lecture du document..."):
        doc_content = read_pdf(uploaded_file)
        st.write("**Contenu du document :**")
        st.text_area("Aperçu du contenu", doc_content[:2000], height=300)  # Limite l'affichage à 2000 caractères

    # Posez une question basée sur le contenu du document
    question = st.text_input("Posez une question basée sur ce document")
    if question:
        if st.button("Analyser"):
            with st.spinner("Analyse en cours..."):
                answer = analyze_document_with_question(doc_content, question)
                st.write("**Réponse :**", answer)

# --- Option sans document ---
else:
    st.write("Ou posez une question directement sans télécharger de fichier.")
    question = st.text_input("Votre question")
    if question:
        if st.button("Poser la question"):
            with st.spinner("Recherche dans la base de données..."):
                answer = retrieve_from_db(question)
                st.write("**Réponse :**", answer)

# --- Historique des conversations ---
st.sidebar.title("Historique des conversations")
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    st.sidebar.write(message)
