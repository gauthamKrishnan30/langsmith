import os
from google import genai

def main():
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    chat = client.chats.create(
        model="gemini-2.5-flash"
    )
    response1 = chat.send_message("What is LLM")
    print("\nResponse 1:\n", response1.text)

    response2 = chat.send_message("Applications of LLM")
    print("\nResponse 2:\n", response2.text)

if __name__ == "__main__":
    main()