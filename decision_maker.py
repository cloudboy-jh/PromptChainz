import openai
import os
from openai import OpenAI
from dotenv import load_dotenv

def prompt_chain_decision_maker():
    """
    Decision Maker prompt - make decisions based on a given scenario.

    Use Case
    - Business Decisions
    - Strategy Planning
    - Problem Solving

    Mermaid Diagram
    A[Start]
    B[Scenario Description]
    C[Decision Making Prompt]
    D[Decision Output]
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

    scenario = "A company wants to expand its product line. They are considering either developing a new AI-powered tool or enhancing an existing product."

    decision_response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Based on the following scenario, make a decision and justify it: {scenario}"}
        ]
    )

    decision_text = decision_response.choices[0].message.content.strip()
    print("Decision: ", decision_text)

if __name__ == "__main__":
    prompt_chain_decision_maker()
