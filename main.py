import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

search_string = input("What u wana Know ?\n")

resp = client.models.generate_content(
    model="gemini-2.0-flash-001", contents=search_string
)

if resp is not None and resp.usage_metadata is not None:
    print(f"Ans: {resp.text} ")
    print(f"prompt_token_count: {resp.usage_metadata.total_token_count}")
    print(f"candidate_token_count: {resp.usage_metadata.candidates_token_count}")
