import openai
import os
from openai import OpenAI
from dotenv import load_dotenv

def prompt_chain_plan_execute():
    """
    Plan and Execute prompt - create a plan and then execute it.

    Use Case
    - Project Management
    - Task Execution
    - Strategic Planning

    Mermaid Diagram
    A[Start]
    B[Plan Creation]
    C[Execute Plan]
    D[End]

    A --> B --> C --> D
    """

    # Load environment variables
    load_dotenv()
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable not set")
    print(f"Using API key: {api_key}")

    # Instantiate the OpenAI client
    client = OpenAI(api_key=api_key)

    task = "organize a webinar on AI ethics."

    plan_response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Create a detailed plan to {task}."}
        ]
    )

    plan_text = plan_response.choices[0].message.content.strip()
    print("Plan: ", plan_text)

    execution_response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Execute the following plan: {plan_text}"}
        ]
    )

    execution_text = execution_response.choices[0].message.content.strip()
    print("Execution: ", execution_text)

if __name__ == "__main__":
    prompt_chain_plan_execute()
