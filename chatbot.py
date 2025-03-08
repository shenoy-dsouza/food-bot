import ollama
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Load the embedding model
embedding_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


def load_faq_data(file_path):
    """
    Load FAQ data from a text file and split it into manageable chunks.
    """
    # print(f"📂 Loading FAQ data from: {file_path}")

    loader = TextLoader(file_path)
    documents = loader.load()

    # Split documents into smaller chunks for better search accuracy
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = text_splitter.split_documents(documents)

    # print(f"✅ Loaded {len(chunks)} FAQ chunks.")
    return chunks


def build_faq_vector_index(file_path):
    """
    Convert FAQ data into numerical embeddings and store them in a FAISS index.
    """
    faq_chunks = load_faq_data(file_path)
    faq_texts = [chunk.page_content for chunk in faq_chunks]

    # print("🔄 Generating embeddings for FAQ data...")

    # Generate vector embeddings using SentenceTransformer
    faq_embeddings = embedding_model.encode(faq_texts).astype(np.float32)

    # print("📌 Storing embeddings in FAISS index...")

    # Create FAISS index for fast similarity search
    index = faiss.IndexFlatL2(faq_embeddings.shape[1])
    index.add(faq_embeddings)

    # print("✅ FAISS index is ready!")
    return index, faq_texts


def retrieve_best_faq_match(user_query, index, faq_texts):
    """
    Retrieve the most relevant FAQ response based on the user's query.
    """
    query_embedding = embedding_model.encode([user_query]).astype(np.float32)
    _, top_match = index.search(query_embedding, k=1)  # Retrieve the top 1 match

    best_match_index = top_match[0][0]
    if best_match_index < len(faq_texts):
        return faq_texts[best_match_index]
    else:
        return "❌ No relevant FAQ found."


def chat_with_ai(file_path):
    """
    Interactive chatbot loop for answering user questions using the FAQ database.
    """
    print(
        "Welcome to FoodBot! Ask about orders, deliveries, payments & more. Type your question or 'exit' to leave."
    )

    # Build the FAISS index
    index, faq_texts = build_faq_vector_index(file_path)

    while True:
        user_query = input("User: ")
        if user_query.lower() == "exit":
            print("👋 Goodbye! Have a great day!")
            break

        # Retrieve the most relevant FAQ response
        faq_response = retrieve_best_faq_match(user_query, index, faq_texts)

        # Generate an AI-based response using Ollama
        prompt = f"Context:\n{faq_response}\n\nUser Query: {user_query}\n\nAnswer:"
        ai_response = ollama.chat(
            model="llama3.2", messages=[{"role": "user", "content": prompt}]
        )

        print(f"Bot: {ai_response['message']['content']}\n")


# Run the chatbot
faq_file = "faq.txt"
chat_with_ai(faq_file)
