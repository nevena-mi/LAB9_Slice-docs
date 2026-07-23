from src.transcription import transcribe_audio
from src.config import AUDIO_PATH


OUTPUT_PATH = "transcripts/podcast_transcript.txt"


print("Using audio file:")
print(AUDIO_PATH)


text = transcribe_audio(
    AUDIO_PATH,
    OUTPUT_PATH
)


print("Transcript created")
print(f"Characters: {len(text)}")