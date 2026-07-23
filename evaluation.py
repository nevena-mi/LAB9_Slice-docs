"""
Functions for evaluating chunking results.
"""


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