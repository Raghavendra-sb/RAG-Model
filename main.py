import os

from pathlib import Path

from dotenv import load_dotenv
load_dotenv()

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# ❌ REMOVE THIS LINE: from langchain_google_genai import GoogleGenerativeAIEmbeddings
# ✅ ADD THIS LINE:
from langchain_huggingface.embeddings import HuggingFaceEmbeddings

from langchain_qdrant import QdrantVectorStore

# ❌ REMOVE THIS SECTION: We don't need the API key anymore
# api_key = os.getenv("GEMINI_API_KEY")

pdf_path = Path(__file__).parent / "nodejs.pdf"

loader = PyPDFLoader(file_path=pdf_path)

docs = loader.load() #read the file 

print(docs[0])

#Chunking
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

split_docs = text_splitter.split_documents(documents=docs)

# ✅ THIS IS THE MAIN CHANGE: Use a local embedding model
# This will download and use the "all-MiniLM-L6-v2" model
# It runs on your computer and requires no API key or payments.
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Your Qdrant setup is correct and stays the same.
# It will work with the new embeddings.
vector_store = QdrantVectorStore.from_documents(
    documents=split_docs,
    url="http://localhost:6333",
    collection_name="learning_vectors",
    embedding=embedding_model,
)

print("Vector Store created successfully")