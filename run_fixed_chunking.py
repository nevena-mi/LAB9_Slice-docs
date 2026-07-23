"""
Run fixed-size character chunking experiment
for podcast transcript and PDF document.
"""


from config import PDF_PATH
from transcript_loader import load_transcript_text
from pdf_loader import load_pdf_text
from chunking import split_text
from evaluation import print_chunk_statistics, check_chunk_endings


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


def main():

    # Load source documents
    podcast_text = load_transcript_text(TRANSCRIPT_PATH)
    pdf_text = load_pdf_text(PDF_PATH)


    # Apply fixed-size chunking
    podcast_chunks = split_text(podcast_text, **PODCAST_SETTINGS)
    pdf_chunks = split_text(pdf_text, **PDF_SETTINGS)


    # Evaluate chunking results
    print_chunk_statistics("Podcast fixed chunks", podcast_chunks)
    print_chunk_statistics("PDF fixed chunks", pdf_chunks)


    print("\nSentence boundary check")
    print("======================")

    print(f"Podcast clean endings: {check_chunk_endings(podcast_chunks):.1f}%")
    print(f"PDF clean endings: {check_chunk_endings(pdf_chunks):.1f}%")


    # Inspect first chunks
    print("\nFirst podcast chunk")
    print("==================")
    print(podcast_chunks[0])


    print("\nFirst PDF chunk")
    print("================")
    print(pdf_chunks[0])


if __name__ == "__main__":
    main()