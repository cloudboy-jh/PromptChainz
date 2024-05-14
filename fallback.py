import openai
import os
from openai import OpenAI
from dotenv import load_dotenv

def prompt_chain_fallback():
    """
    Fallback prompt - use a backup model if the primary model fails to deliver a satisfactory response.

    Use Case
    - Reliability
    - Redundancy
    - Error Handling

    Mermaid Diagram
    A[Start]
    B[Primary Model Prompt]
    C{Is Response Satisfactory?}
    D[Fallback Model Prompt]
    E[End]

    A --> B --> C
    C -->|Yes| E
    C -->|No| D --> E
    """

    # Load environment variables
    load_dotenv()
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable not set")
    print(f"Using API key: {api_key}")

    # Instantiate the OpenAI client
    client = OpenAI(api_key=api_key)

    # Model names can be adjusted as needed
    haiku_model = "gpt-3.5-turbo"
    sonnet_model = "gpt-3.5-turbo"

    primary_response = client.chat.completions.create(
        model=haiku_model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Explain the significance of data privacy in AI applications."}
        ]
    )

    primary_text = primary_response.choices[0].message.content.strip()

    if "error" in primary_text.lower() or not primary_text:
        fallback_response = client.chat.completions.create(
            model=sonnet_model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Explain the significance of data privacy in AI applications."}
            ]
        )
        fallback_text = fallback_response.choices[0].message.content.strip()
        print("Fallback Response: ", fallback_text)
    else:
        print("Primary Response: ", primary_text)

if __name__ == "__main__":
    prompt_chain_fallback()
