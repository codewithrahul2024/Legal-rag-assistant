from pathlib import Path
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

from document_loader import load_legal_document
from chunking import create_chunks


PERSIST_DIRECTORY = Path("chroma_db")


def create_vector_store():
    documents = load_legal_document()
    chunks = create_chunks(documents)

    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small"
    )

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=str(PERSIST_DIRECTORY),
        collection_name="indian_law"
    )

    print("Vector database created successfully.")

    return vector_store


if __name__ == "__main__":
    create_vector_store()
