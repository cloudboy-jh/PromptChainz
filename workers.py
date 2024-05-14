import openai
import os
from openai import OpenAI
from dotenv import load_dotenv

def prompt_chain_workers():
    """
    Workers prompt - distribute tasks among different models, each handling a specific task.

    Use Case
    - Complex Tasks
    - Work Distribution
    - Parallel Processing

    Mermaid Diagram
    A[Start]
    B[Task Assignment]
    C[Model 1 Execution]
    D[Model 2 Execution]
    E[Model 3 Execution]
    F[Combine Results]
    G[End]

    A --> B --> C --> F --> G
    B --> D --> F
    B --> E --> F
    """

    # Load environment variables
    load_dotenv()
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable not set")
    print(f"Using API key: {api_key}")
    
    # Instantiate the OpenAI client
    client = OpenAI(api_key=api_key)

    task_1 = "Generate a detailed introduction about the importance of AI in healthcare."
    task_2 = "Provide a technical overview of AI algorithms used in image recognition."
    task_3 = "Discuss future trends of AI in healthcare."

    # Model names can be adjusted as needed
    haiku_model = "gpt-3.5-turbo"
    sonnet_model = "gpt-3.5-turbo"
    opus_model = "gpt-3.5-turbo"

    # Model 1 Execution
    intro_response = client.chat.completions.create(
        model=haiku_model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Create an introduction: {task_1}"}
        ]
    )

    # Model 2 Execution
    tech_overview_response = client.chat.completions.create(
        model=sonnet_model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Create a technical overview: {task_2}"}
        ]
    )

    # Model 3 Execution
    future_trends_response = client.chat.completions.create(
        model=opus_model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Create future trends discussion: {task_3}"}
        ]
    )

    combined_results = f"Introduction:\n{intro_response.choices[0].message.content.strip()}\n\nTechnical Overview:\n{tech_overview_response.choices[0].message.content.strip()}\n\nFuture Trends:\n{future_trends_response.choices[0].message.content.strip()}"

    print("Combined Results: ", combined_results)

if __name__ == "__main__":
    prompt_chain_workers()
