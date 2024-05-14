import openai
import os
import random
import json
from dotenv import load_dotenv
import subprocess

def prompt_chain_self_correct():
    """
    Self-correct prompt - generate an initial output, check for errors, and correct if necessary.

    Use Case
    - Error Correction
    - Validation
    - Iterative Improvement

    Mermaid Diagram
    A[Start]
    B[Generate Initial Prompt]
    C[Execute Output]
    D[Self Correct]
    E[End]

    A --> B --> C --> D --> E
    C --> E
    """

    def run_bash(command):
        print(f"Running command: {command}")
        try:
            result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return result.stdout.decode('utf-8')
        except subprocess.CalledProcessError as e:
            return f"Error: {e.stderr.decode('utf-8')}"

    # Load environment variables
    load_dotenv()
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable not set")
    print(f"Using API key: {api_key}")

    # Set OpenAI API key
    openai.api_key = api_key

    outcome = "list all files in the current directory"

    initial_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Generate a bash command that enables us to {outcome}. Respond with only the command."}
        ]
    )
    initial_text = initial_response['choices'][0]['message']['content'].strip()
    print(f"Initial response: {initial_text}")

    # Run the generated command and check for errors
    result = run_bash(initial_text)

    if "error" in result.lower():
        print("Received error, running self-correction prompt")

        # If error, run self-correction prompt
        self_correct_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"The following bash command was generated to {outcome}, but encountered an error when run:\n\nCommand: {initial_text}\nError: {result}\n\nPlease provide an updated bash command that will successfully {outcome}. Respond with only the updated command in JSON format {{\"command\": \"<command>\"}}."}
            ]
        )
        self_correct_text = self_correct_response['choices'][0]['message']['content'].strip()
        print(f"Self-corrected response: {self_correct_text}")

        # Parse the JSON response to get the command
        try:
            self_corrected_command = json.loads(self_correct_text).get("command")
            if self_corrected_command:
                run_bash(self_corrected_command)
            else:
                print("Error: Unable to parse the corrected command.")
        except json.JSONDecodeError as e:
            print(f"JSON decode error: {e}")

    else:
        print(f"Original command executed successfully: {result}")

if __name__ == "__main__":
    prompt_chain_self_correct()
