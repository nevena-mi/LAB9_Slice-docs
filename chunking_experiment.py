"""
Chunking experiment:
Compare fixed-size chunking for:
1. Podcast transcript
2. PDF document

The experiment allows independent chunk sizes
for each document type.
"""


# -----------------------------
# Imports
# -----------------------------

from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader

from src.chunking import split_text



# -----------------------------
# File paths
# -----------------------------

PDF_PATH = "data/385082eng.pdf"

TRANSCRIPT_PATH = "transcripts/podcast_transcript.txt"



# -----------------------------
# Chunking configuration
# Independent settings for each source
# -----------------------------

PODCAST_SETTINGS = {
    "chunk_size": 300,
    "chunk_overlap": 100,
    "separator": "\n"
}


PDF_SETTINGS = {
    "chunk_size": 200,
    "chunk_overlap": 100,
    "separator": "\n"
}

# Load podcast transcript
def load_transcript(path):

    """
    Load previously generated Whisper transcript.
    Returns plain text.
    """

    with open(path, "r", encoding="utf-8") as file:
        text = file.read()

    return text


# Load PDF document
def load_pdf(path):

    """
    Load PDF using LangChain.
    Returns combined text from all pages.
    """

    loader = PyPDFLoader(path)

    documents = loader.load()

    # Each PDF page is a separate Document object.
    # We combine all page contents into one text string.
    text = "\n".join(
        page.page_content
        for page in documents
    )

    return text

# Run chunking experiment
def main():

    # Load sources
    podcast_text = load_transcript(
        TRANSCRIPT_PATH
    )

    pdf_text = load_pdf(
        PDF_PATH
    )


    print("\nLoaded documents")
    print("----------------")
    print(
        f"Podcast characters: {len(podcast_text)}"
    )
    print(
        f"PDF characters: {len(pdf_text)}"
    )

    # Split podcast transcript
    podcast_chunks = split_text(
        podcast_text,
        **PODCAST_SETTINGS
    )

    # Split PDF
    pdf_chunks = split_text(
        pdf_text,
        **PDF_SETTINGS
    )

    # Inspect results
    print("\nChunking results")
    print("----------------")

    print(
        f"Podcast chunks: {len(podcast_chunks)}"
    )

    print(
        f"PDF chunks: {len(pdf_chunks)}"
    )


    # Show examples

    print("\nFirst podcast chunk")
    print("------------------")
    print(
        podcast_chunks[0][:500]
    )


    print("\nFirst PDF chunk")
    print("------------------")
    print(
        pdf_chunks[0][:500]
    )


# Run script
if __name__ == "__main__":
    main()