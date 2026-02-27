# ── Imports ────────────────────────────────────────────────
import os
import logging
from dotenv import load_dotenv
# LangChain
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_groq import ChatGroq
from langchain_community.embeddings import HuggingFaceEmbeddings
# Gradio
import gradio as gr
from gradio_styling import KUSH_CSS, create_kush_header



# ── Logging setup ──────────────────────────────────────────
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ── Configuration ──────────────────────────────────────────
load_dotenv()
PDF_PATH = "thesis.pdf"
CHUNK_SIZE = 500
CHUNK_OVERLAP = 100
MODEL_NAME = "llama-3.3-70b-versatile"  # free Groq model
EMBEDDING_MODEL = "all-MiniLM-L6-v2" # embedding model

# ── LLM Initialisation ──────────────────────────────────────────
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Check if key exists to clear Pylance 'None' warnings
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found. Please check your .env file.")

llm = ChatGroq(
    model=MODEL_NAME,

)

# –– RAG Pipeline Function ––––––––––––––––––––––––––––––––––
def build_rag_chain():
    # Step 1: Load PDF
    loader = PyPDFLoader(PDF_PATH)
    thesis = loader.load()

    # Step 2: Chunk it
    text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=CHUNK_SIZE,
    chunk_overlap=CHUNK_OVERLAP,
    separators=["\n\n", "\n", ". ", " ", ""]
    )
    chunks_thesis = text_splitter.split_documents(thesis)

    # Step 3: Embed and store in ChromaDB
    embedding_model = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
    vector_store = Chroma.from_documents(chunks_thesis, embedding_model)
    retriever = vector_store.as_retriever()

    # Step 4: Build RAG chain
    template = """You are a professional personal assistant. 
    Use ONLY the following context to answer the question.
    If the answer is not in the context, say "I don't have enough information to answer this."
    Give a concise answer in 3-4 sentences maximum.

    Context: {context}

    Question: {question}

    Answer:"""

    prompt=PromptTemplate.from_template(template)

    chain = (
    {"context": retriever, "question": RunnablePassthrough()} 
    | prompt 
    | llm 
    | StrOutputParser()
    )

    # Step 5: Return the chain
    return chain

chain = build_rag_chain()

def chat(message, history):
    return chain.invoke(message)


with gr.Blocks(css=KUSH_CSS, title="Ask My Thesis") as demo:
    # Call the header from your styling file
    create_kush_header()
    
    gr.ChatInterface(
        fn=chat,
        chatbot=gr.Chatbot(
            elem_id="chatbot", 
            bubble_full_width=False, 
            height=600,
            show_label=False
        ),
        textbox=gr.Textbox(
            elem_id="textbox",
            placeholder="TYPE YOUR INQUIRY...", 
            container=False, 
            scale=7
        ),
        theme=gr.themes.Monochrome()
    )

if __name__ == "__main__":
    demo.launch()