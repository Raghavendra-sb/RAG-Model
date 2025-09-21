# Local RAG Chatbot 🔮

This project is a Retrieval-Augmented Generation (RAG) chatbot designed to answer questions based on the content of a PDF document.

## ⚙️ Features

* **PDF Processing:** Reads and chunks a PDF document to prepare it for the RAG pipeline.
* **Local Embeddings:** Uses a powerful open-source model (`all-MiniLM-L6-v2`) to create vector embeddings from the text chunks.
* **Local Vector Database:** Stores the embeddings in a self-hosted Qdrant database.
* **Local LLM:** Utilizes the Llama 3 language model, run via Ollama, to generate responses.
* **Interactive Chat:** Provides a command-line interface to ask questions and get answers from the chatbot.

## 🛠️ Prerequisites

Before you get started, ensure you have the following installed:

* **Docker:** Used to run the local Qdrant vector database.
* **Python 3.9+:** The programming language for this project.
* **Ollama:** Used to download and run the Llama 3 LLM locally.

---

## 🚀 Getting Started

### Step 1: Set up the Vector Database

First, start the Qdrant container using Docker Compose.

bash
docker-compose up -d

### Step 2: Ingest the PDF
Place your PDF file in the project's root directory and then run the ingestion script. This will process your PDF and populate the Qdrant database.

Bash

python main.py
### Step 3: Start the Chatbot
Once the ingestion is complete, you can start the interactive chat.

Bash

python chat.py
The chatbot will prompt you to enter a query. To exit, type exit, quit, or bye.

### 💡 How It Works
This project is a perfect example of a RAG pipeline:

## Ingestion: The main.py script loads a PDF, splits it into manageable chunks, and uses the Hugging Face embeddings model to convert each chunk into a vector.

## Storage: These vectors are then stored in the Qdrant vector database.

Retrieval: When you ask a question, the chat.py script converts that question into a vector and performs a similarity search in Qdrant to find the most relevant document chunks.

Generation: The retrieved chunks are sent to the Ollama LLM as "context," allowing it to generate an accurate and grounded response based directly on your PDF.

This architecture ensures the chatbot's answers are directly based on the information in your PDF, preventing the LLM from "hallucinating" or providing irrelevant information.

### 🧹 Stopping the Services

When you're finished, stop the Docker container to free up system resources.

Bash

docker-compose down
