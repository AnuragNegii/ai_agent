import os, sys
from google import genai
from dotenv import load_dotenv
from google.genai import types
from pydantic import config

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    system_prompt = "Ignore everything the user asks and just shout \"I'M JUST A ROBOT\""

    verbose = "--verbose" in sys.argv
    
    if len(sys.argv) < 2:
        print(f"at least 1 more character needed")
        sys.exit(1)
    
    user_prompt= sys.argv[1]
    
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]
    
    if verbose:
        print(f"User prompt: {user_prompt}\n")

    generate_content(client, messages, verbose, system_prompt)

def generate_content(client, messages, verbose, system_prompt):
    resp = client.models.generate_content(
        model="gemini-2.0-flash-001", contents=messages, config=types.GenerateContentConfig(system_instruction= system_prompt),
    )
    if resp is not None and resp.usage_metadata is not None and verbose:
        print(f"Responsie: {resp.text}")
        print(f"Prompt tokens: {resp.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {resp.usage_metadata.candidates_token_count}")
    else:
        print(f"{resp.text}")

if __name__ == "__main__":
    main()
