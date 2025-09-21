import os

# New, non-deprecated imports
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.chat_models import ChatOllama
from langchain_qdrant import QdrantVectorStore

# Your existing code to set up the models and DB connection
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_db = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="learning_vectors",
    embedding=embedding_model,
)

ollama_llm = ChatOllama(model="llama3")

# --- THIS IS THE NEW PART ---
# The while loop will keep the script running
while True:
    # Take User Query
    query = input("> ")

    # Add a way to exit the chat
    if query.lower() in ['exit', 'quit', 'bye']:
        print("🤖: Goodbye!")
        break # This command exits the while loop

    # Vector Similarity Search
    search_results = vector_db.similarity_search(query=query)

    # Prepare the context
    context = "\n\n".join(
        [f"Page Content: {result.page_content}\nPage Number: {result.metadata['page_label']}" for result in search_results]
    )

    SYSTEM_PROMPT = f"""
        You are a helpful AI assistant who answers user queries based on the available context retrieved from a PDF file along with page_contents and page number.

        You should only answer the user based on the following context and navigate the user to open the right page number to know more.

        Context:
        {context}
    """

    # Generate the response using Ollama
    response = ollama_llm.invoke(
        [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": query}
        ]
    )

    print(f"🤖: {response.content}")