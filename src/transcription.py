# function returns plain text, not the API object

def transcribe_audio(client, audio_path):

    with open(audio_path, "rb") as audio_file:

        response = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )

    return response.text