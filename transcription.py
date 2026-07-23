from pathlib import Path

from config import get_openai_client



def transcribe_audio(
        audio_path,
        output_path,
        model="whisper-1"
        ):
    """Transcribe audio using OpenAI Whisper and save transcript."""


    # Create authenticated OpenAI client
    client = get_openai_client()

    # Convert paths to Path objects
    audio_path = Path(audio_path)
    output_path = Path(output_path)

    # Send audio file to Whisper
    with open(audio_path, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model=model,
            file=audio_file
        )

    # Extract text
    transcript_text = transcript.text

    # Save transcript
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(transcript_text)

    return transcript_text