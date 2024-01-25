from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()


def get_gpt_response(text: str, role: str = '', temperature: float = 0.5):
    completion = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": f'{text}'}
        ],
        temperature=temperature,
    )

    return completion.choices[0].message.content
