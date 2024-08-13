#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

from dotenv import load_dotenv
import os
import openai

os.environ

os.environ["OPENAI_API_KEY"] = "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"

print(os.environ.get("OPENAI_API_KEY"))

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

openai.api_key= api_key

completion = openai.ChatCompletion.creat(
    model = "gpt-3.5-turbo",
    messages = [
        {"role": "user", "content": "Hello!"}
    ]
)
