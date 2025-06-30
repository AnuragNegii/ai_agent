import os, sys
from google import genai
from dotenv import load_dotenv
from google.genai import types

from prompts import system_prompt
from call_function import available_functions, call_function


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
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

    generate_content(client, messages, verbose)

def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction= system_prompt
        ),
    )
    if verbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)
    if not response.function_calls:
        return response.textrbose
    function_responses=[]
    for function_call_part in response.function_calls:
        function_call_result = call_function(function_call_part, verbose)
        if (not function_call_result.parts or not function_call_result.parts[0].function_response):
            raise Exception("Empty function call result")
        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")
        function_responses.append(function_call_result.parts[0])
    if  not function_responses:
        raise Exception("No function responses generated, exiting.")

if __name__ == "__main__":
    main()
