from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader

PDF_PATH = Path("data/bns_2023.pdf")


def load_legal_document():
    if not PDF_PATH.exists():
        raise FileNotFoundError(
            f"PDF file not found: {PDF_PATH}"
        )

    loader = PyPDFLoader(str(PDF_PATH))
    documents = loader.load()

    print(f"Loaded {len(documents)} pages.")

    return documents


if __name__ == "__main__":
    documents = load_legal_document()

    print("\nFirst page preview:\n")
    print(documents[0].page_content[:2000])

    print("\nMetadata:\n")
    print(documents[0].metadata)
