def load_transcript_text(transcript_path):
    """Load podcast transcript and return text."""

    # Read transcript file created by Whisper
    with open(transcript_path, "r", encoding="utf-8") as file:
        text = file.read()

    return text