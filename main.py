from summarizer.pipeline import run_pipeline


if __name__ == "__main__":
    summary = run_pipeline("data/sales.csv")
    print("\nAI-Generated Summary:\n")
    print(summary)
