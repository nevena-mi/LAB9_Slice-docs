# debugging

def inspect_text(name, text, length=500):

    print(f"\n--- {name} ---")
    print("Type:", type(text))
    print("Length:", len(text))
    print(text[:length])


def inspect_chunks(name, chunks, number=3):

    print(f"\n--- {name} chunks ---")
    print("Number of chunks:", len(chunks))


    for i, chunk in enumerate(chunks[:number]):

        print(f"\nChunk {i}")
        print("Length:", len(chunk))
        print(chunk[:300])


def inspect_endings(chunks, number=5):

    print("\n--- Chunk endings ---")

    for i, chunk in enumerate(chunks[:number]):

        print(
            f"Chunk {i}:",
            repr(chunk[-50:])
        )