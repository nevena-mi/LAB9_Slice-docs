# PDF extraction

from langchain_community.document_loaders import PyPDFLoader


def load_pdf_text(pdf_path):

    loader = PyPDFLoader(pdf_path)

    documents = loader.load()

    text = "\n".join(
        doc.page_content
        for doc in documents
    )

    return text, documents