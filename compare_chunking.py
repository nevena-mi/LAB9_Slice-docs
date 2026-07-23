"""
Compare different chunking strategies.

Strategies:
1. Fixed character chunking
2. Recursive character chunking
3. Token-based chunking
"""

import matplotlib.pyplot as plt

from pdf_loader import load_pdf_text
from transcript_loader import load_transcript_text
from chunking import (
    split_text,
    split_text_recursive,
    split_text_token
)
from evaluation import check_chunk_endings


from config import PDF_PATH


TRANSCRIPT_PATH = "transcripts/podcast_transcript.txt"


FIXED_SETTINGS = {
    "chunk_size": 500,
    "chunk_overlap": 100,
    "separator": " "
}

RECURSIVE_SETTINGS = {
    "chunk_size": 500,
    "chunk_overlap": 100
}

TOKEN_SETTINGS = {
    "chunk_size": 500,
    "chunk_overlap": 100
}


def get_statistics(chunks):
    """Calculate chunk statistics."""

    sizes = [len(chunk) for chunk in chunks]

    return {
        "Average size": round(sum(sizes) / len(sizes), 1),
        "Minimum": min(sizes),
        "Maximum": max(sizes),
        "Number of chunks": len(chunks),
        "Sentence endings %": round(
            check_chunk_endings(chunks), 1
        )
    }


def plot_distribution(name, chunks):
    """Plot chunk size distribution."""

    sizes = [len(chunk) for chunk in chunks]

    plt.hist(sizes, bins=20)

    plt.xlabel("Chunk size (characters)")
    plt.ylabel("Frequency")
    plt.title(name)

    plt.savefig(
        f"outputs/{name}.png",
        bbox_inches="tight"
    )

    plt.show()

    plt.close()


def compare_strategies(text, name):

    fixed = split_text(
        text,
        **FIXED_SETTINGS
    )

    recursive = split_text_recursive(
        text,
        **RECURSIVE_SETTINGS
    )

    token = split_text_token(
        text,
        **TOKEN_SETTINGS
    )

    strategies = {
        "Fixed": fixed,
        "Recursive": recursive,
        "Token": token
    }

    print(f"\n{name}")
    print("=" * len(name))

    print(
        f"{'Strategy':<12}"
        f"{'Avg':<10}"
        f"{'Min':<10}"
        f"{'Max':<10}"
        f"{'Chunks':<10}"
        f"{'Ends %'}"
    )

    for strategy, chunks in strategies.items():

        stats = get_statistics(chunks)

        print(
            f"{strategy:<12}"
            f"{stats['Average size']:<10}"
            f"{stats['Minimum']:<10}"
            f"{stats['Maximum']:<10}"
            f"{stats['Number of chunks']:<10}"
            f"{stats['Sentence endings %']}"
        )

    return strategies


def main():

    podcast_text = load_transcript_text(
        TRANSCRIPT_PATH
    )

    pdf_text = load_pdf_text(
        PDF_PATH
    )


    podcast_results = compare_strategies(
        podcast_text,
        "Podcast"
    )

    pdf_results = compare_strategies(
        pdf_text,
        "PDF"
    )


    for strategy, chunks in podcast_results.items():
        plot_distribution(
            f"Podcast - {strategy}",
            chunks
        )

    for strategy, chunks in pdf_results.items():
        plot_distribution(
            f"PDF - {strategy}",
            chunks
        )


    print("\nChunk ending examples")
    print("====================")

    print("\nPodcast recursive ending:")
    print(
        podcast_results["Recursive"][0][-50:]
    )

    print("\nPDF recursive ending:")
    print(
        pdf_results["Recursive"][0][-50:]
    )


if __name__ == "__main__":
    main()