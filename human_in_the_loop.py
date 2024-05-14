import openai
import os
from openai import OpenAI
from dotenv import load_dotenv

def prompt_chain_human_in_the_loop():
    """
    Human-in-the-Loop prompt - involve human input at critical stages.

    Use Case
    - Quality Assurance
    - Collaborative Work
    - Iterative Development

    Mermaid Diagram
    A[Start]
    B[Initial Prompt]
    C[Human Input]
    D[Refinement Prompt]
    E[End]

    A --> B --> C --> D --> E
    """

    # Load environment variables
    load_dotenv()
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable not set")
    print(f"Using API key: {api_key}")

    # Instantiate the OpenAI client
    client = OpenAI(api_key=api_key)

    initial_prompt = "Draft a policy on remote work."

    draft_response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Draft an initial policy: {initial_prompt}"}
        ]
    )

    draft_text = draft_response.choices[0].message.content.strip()
    print("Draft: ", draft_text)

    human_input = input("Provide your feedback on the draft: ")

    refined_response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Refine the policy based on the following feedback: {human_input}"}
        ]
    )

    refined_text = refined_response.choices[0].message.content.strip()
    print("Refined Policy: ", refined_text)

if __name__ == "__main__":
    prompt_chain_human_in_the_loop()
