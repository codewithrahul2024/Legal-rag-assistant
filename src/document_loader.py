from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader


# Path to the legal document
PDF_PATH = Path("data/eu_ai_act.pdf")


def load_legal_document():
    """
    Load the EU AI Act PDF and return the extracted documents.
    Each page is returned as a separate LangChain Document.
    """

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
