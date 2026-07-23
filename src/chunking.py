# Import LangChain's character-based text splitter.
# This splitter divides a long text into smaller pieces (chunks)
# based on the number of characters.
from langchain_text_splitters import CharacterTextSplitter


# This function creates and configures a text splitter object.
# It does not split the text yet; it only defines the rules
# that will be used for splitting.
def create_character_splitter(
        chunk_size=500,        # Maximum number of characters in each chunk
        chunk_overlap=0,       # Number of characters repeated between neighboring chunks
        separator="\n"         # Where the splitter tries to split first (here: new lines)
):

    # Create a CharacterTextSplitter instance with the chosen settings.
    # The returned object knows HOW to split text.
    return CharacterTextSplitter(
        separator=separator,
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )


# This function takes actual text and splits it into chunks.
# It combines the creation of the splitter and the splitting operation
# into one reusable function.
def split_text(
        text,                  # The document text that should be divided into chunks
        chunk_size=500,        # Desired chunk size
        chunk_overlap=0,       # Amount of repeated text between chunks
        separator="\n"         # Preferred splitting boundary
):

    # First create a splitter with the requested parameters.
    # Example:
    # chunk_size=1000 for PDF
    # chunk_size=500 for podcast transcript
    splitter = create_character_splitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separator=separator
    )


    # Apply the splitter to the text.
    # The result is a list where each element is one chunk of text.
    chunks = splitter.split_text(text)


    # Return the generated chunks so they can be inspected,
    # analyzed, embedded, or used in a retrieval system.
    return chunks