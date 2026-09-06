from document_loader import load_legal_document
from langchain_text_splitters import RecursiveCharacterTextSplitter


def create_chunks(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(documents)

    print(f"Created {len(chunks)} chunks.")

    return chunks


if __name__ == "__main__":
    documents = load_legal_document()
    chunks = create_chunks(documents)

    print("\nFirst chunk:\n")
    print(chunks[0].page_content)

    print("\nMetadata:\n")
    print(chunks[0].metadata)
