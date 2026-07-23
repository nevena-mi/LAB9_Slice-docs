from langchain_text_splitters import (
    CharacterTextSplitter,
    RecursiveCharacterTextSplitter,
    TokenTextSplitter
)

# Creates and configures a text splitter object
def create_character_splitter(
        chunk_size=500,
        chunk_overlap=0,
        separator="\n"
):
    """Create a character-based text splitter."""

    # Defines how text will be divided into chunks
    return CharacterTextSplitter(
        separator=separator,
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )


def split_text(
        text,
        chunk_size=500,
        chunk_overlap=0,
        separator="\n"
):
    """Split text using CharacterTextSplitter."""

    # Create splitter with chosen parameters
    splitter = create_character_splitter(
        chunk_size,
        chunk_overlap,
        separator
    )

    # Apply splitting and return list of chunks
    return splitter.split_text(text)


def create_recursive_splitter(
        chunk_size=500,
        chunk_overlap=100,
        separators=None
):
    """Create a RecursiveCharacterTextSplitter."""

    # Separators are tried in order to preserve structure
    if separators is None:
        separators = ["\n\n", "\n", ". ", " ", ""]

    return RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=separators
    )


def split_text_recursive(
        text,
        chunk_size=500,
        chunk_overlap=100,
        separators=None
):
    """Split text using recursive character splitting."""

    splitter = create_recursive_splitter(
        chunk_size,
        chunk_overlap,
        separators
    )

    return splitter.split_text(text)

# Creates and configures a token-based text splitter object.
def create_token_splitter(
        chunk_size=500,
        chunk_overlap=100
):
    """Create a token-based text splitter."""

    return TokenTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )


def split_text_token(
        text,
        chunk_size=500,
        chunk_overlap=100
):
    """Split text using token-based chunking."""

    splitter = create_token_splitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    return splitter.split_text(text)