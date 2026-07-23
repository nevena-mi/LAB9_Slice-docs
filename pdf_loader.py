from langchain_community.document_loaders import PyPDFLoader


def load_pdf_text(pdf_path):
    """Load PDF and return extracted text with page documents."""

    # Load PDF pages as LangChain Document objects
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    # Combine all pages into one text string for chunking
    text = "\n".join(
        doc.page_content
        for doc in documents
    )

    # Return both:
    # - text for chunking experiments
    # - documents if page metadata is needed later
    return text