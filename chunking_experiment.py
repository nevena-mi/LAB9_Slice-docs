"""
Chunking experiment:
Compare fixed-size chunking for:
1. Podcast transcript
2. PDF document

Allows independent chunk sizes and overlap values
for each document type.
"""

from langchain_community.document_loaders import PyPDFLoader

from src.chunking import split_text, split_text_recursive
from src.config import PDF_PATH


TRANSCRIPT_PATH = "transcripts/podcast_transcript.txt"


PODCAST_SETTINGS = {
    "chunk_size": 300,
    "chunk_overlap": 100,
    "separator": " "
    }

PDF_SETTINGS = {
    "chunk_size": 500,
    "chunk_overlap": 100,
    "separator": "\n"
    }

RECURSIVE_PODCAST_SETTINGS = {
    "chunk_size": 300,
    "chunk_overlap": 50
    }

RECURSIVE_PDF_SETTINGS = {
    "chunk_size": 300,
    "chunk_overlap": 50
    }


def load_transcript(path):
    """Load Whisper-generated transcript as plain text."""

    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def load_pdf(path):
    """Load PDF and combine all pages into one text string."""

    documents = PyPDFLoader(path).load()

    return "\n".join(
        document.page_content
        for document in documents
    )


def print_chunk_statistics(name, chunks):
    """Print basic chunk size statistics."""

    sizes = [len(chunk) for chunk in chunks]

    print(f"\n{name}")
    print("-" * len(name))
    print(f"Number of chunks: {len(chunks)}")
    print(f"Average size: {sum(sizes) / len(sizes):.1f} characters")
    print(f"Smallest chunk: {min(sizes)} characters")
    print(f"Largest chunk: {max(sizes)} characters")

def check_chunk_endings(chunks):
    """Calculate percentage of chunks ending at sentence boundaries."""

    clean = sum(
        1
        for chunk in chunks
        if chunk.strip()[-1] in ".?!"
    )

    return clean / len(chunks) * 100   


def main():

    podcast_text = load_transcript(TRANSCRIPT_PATH)
    pdf_text = load_pdf(PDF_PATH)

    print("Loaded documents")
    print("================")
    print(f"Podcast characters: {len(podcast_text)}")
    print(f"PDF characters: {len(pdf_text)}")


    podcast_chunks = split_text(
        podcast_text,
        **PODCAST_SETTINGS
        )

    pdf_chunks = split_text(
        pdf_text,
        **PDF_SETTINGS
        )

    recursive_podcast_chunks = split_text_recursive(
        podcast_text,
        **RECURSIVE_PODCAST_SETTINGS)

    recursive_pdf_chunks = split_text_recursive(
        pdf_text,
        **RECURSIVE_PDF_SETTINGS)


    print_chunk_statistics("Podcast chunks", podcast_chunks)
    print_chunk_statistics("PDF chunks", pdf_chunks)

    print("\nSentence boundary check")
    print("======================")

    print(
    f"Podcast clean endings: {check_chunk_endings(podcast_chunks):.1f}%")

    print(f"PDF clean endings: {check_chunk_endings(pdf_chunks):.1f}%")


    print("\nFirst podcast chunk")
    print("==================")
    print(podcast_chunks[0])


    print("\nFirst PDF chunk")
    print("================")
    print(pdf_chunks[0])


    print("\nChunk endings inspection")
    print("=======================")

    print("\nPodcast last characters:")
    print(podcast_chunks[0][-100:])

    print("\nPDF last characters:")
    print(pdf_chunks[0][-100:])

    print("\nRecursive podcast ending")
    print("========================")
    print(recursive_podcast_chunks[0][-100:])

    print("\nRecursive PDF ending")
    print("===================")
    print(recursive_pdf_chunks[0][-100:])


if __name__ == "__main__":
    main()