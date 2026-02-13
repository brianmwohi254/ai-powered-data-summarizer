import os
from openai import OpenAI


class AISummarizer:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def summarize(self, structured_data: str) -> str:
        """Generate a business summary from structured text."""
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a business analyst."},
                {
                    "role": "user",
                    "content": f"Summarize this revenue data:\n{structured_data}",
                },
            ],
        )

        return response.choices[0].message.content
