from pathlib import Path

from langchain_chroma import Chroma
from langchain_core.documents import Document

from embeddings import get_embeddings


DB_DIR = "data/chroma"
DOCUMENT_DIR = Path("data/documents")

def load_documents():
    documents = []

    for file_path in DOCUMENT_DIR.glob("*.txt"):
        text = file_path.read_text(encoding="utf-8").strip()

        if not text:
            continue

        documents.append(
            Document(
                page_content=text,
                metadata={
                    "source": file_path.name
                }
            )
        )

    if not documents:
        raise ValueError(
            f"No .txt documents found in {DOCUMENT_DIR.resolve()}"
        )

    return documents


def create_vectorstore():

    documents = load_documents()

    embeddings = get_embeddings()

    vectorstore = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory=DB_DIR,
        collection_name="sales_documents"
    )

    return vectorstore