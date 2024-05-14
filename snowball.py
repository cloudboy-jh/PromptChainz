import openai
import os
from openai import OpenAI
from dotenv import load_dotenv

def prompt_chain_snowball():
    # Load environment variables
    load_dotenv()
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable not set")
    print(f"Using API key: {api_key}")
    
    # Instantiate the OpenAI client
    client = OpenAI(api_key=api_key)
    
    base_information = "3 facts about cats"

    try:
        # Snowball Prompt 1
        snowball_prompt_response_1 = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Generate a clickworthy title about this topic: '{base_information}'."}
            ]
        )
        response_1_text = snowball_prompt_response_1.choices[0].message.content.strip()
        print("Snowball #1: ", response_1_text)

        # Snowball Prompt 2
        snowball_prompt_response_2 = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Generate a compelling 3 section outline given this information: '{response_1_text}'."}
            ]
        )
        response_2_text = snowball_prompt_response_2.choices[0].message.content.strip()
        print("Snowball #2: ", response_2_text)

        # Snowball Prompt 3
        snowball_prompt_response_3 = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Generate 1 paragraph of content for each section outline given this information: '{response_2_text}'."}
            ]
        )
        response_3_text = snowball_prompt_response_3.choices[0].message.content.strip()
        print("Snowball #3: ", response_3_text)

        return response_1_text, response_2_text, response_3_text

    except openai.OpenAIError as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    prompt_chain_snowball()
 