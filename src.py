from google import genai
from langsmith import wrappers
import os

def main():
    gemini_client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    client = wrappers.wrap_gemini(
        gemini_client,
        tracing_extra={
            "tags": ["gemini-direct", "example-1"],
            "metadata": {"integration": "google-genai", "model": "gemini-2.5-flash"}
        }
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[{"role": "user", "parts": [{"text": "what is llm?"}]}]
    )

    print(response.text)

if __name__ == "__main__":
    main()