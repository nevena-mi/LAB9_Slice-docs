import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


#AUDIO_PATH = "data/Red_Lines_and_Risks_in_the_AI_Act.m4a"
PDF_PATH = "data/385082eng.pdf"
AUDIO_PATH = (
    "data/Red_Lines_and_Risks_in_the_AI_Act_small.m4a"
)


def get_openai_client():
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError("OPENAI_API_KEY is missing")

    return OpenAI(api_key=api_key)