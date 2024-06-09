from groq import Groq
from dotenv import load_dotenv
import os
from config import model

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def get_resp(msgs):
    response = client.chat.completions.create(model=model, messages=msgs)
    return response.choices[0].message.content
