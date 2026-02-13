from summarizer.cleaner import load_data, clean_data
from summarizer.ai_client import AISummarizer


def run_pipeline(filepath: str) -> str:
    df = load_data(filepath)
    cleaned = clean_data(df)

    structured_text = cleaned.to_string(index=False)

    ai = AISummarizer()
    summary = ai.summarize(structured_text)

    return summary
