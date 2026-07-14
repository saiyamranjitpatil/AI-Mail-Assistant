import requests

from config import OLLAMA_MODEL, OLLAMA_URL


def summarize_email(email_body, priority):
    """
    Sends an email to the local Qwen model
    and returns an AI-generated analysis.
    """

    # Limit email size for faster processing
    email_body = email_body[:1500]

    prompt = f"""
You are an Executive AI Email Assistant.

Python has already determined the email priority.

Priority: {priority}

Do NOT change the priority.

Your task is to analyze the email and return ONLY in the following format.

Category:

Summary:
- Point 1
- Point 2
- Point 3

Action Required:

Deadline:

Email:

{email_body}
"""

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": OLLAMA_MODEL,
                "prompt": prompt,
                "stream": False
            },
            timeout=120
        )

        response.raise_for_status()

        result = response.json()

        return result.get("response", "No response received from the AI.")

    except requests.exceptions.Timeout:
        return "Error: Ollama timed out."

    except requests.exceptions.ConnectionError:
        return "Error: Could not connect to Ollama."

    except Exception as e:
        return f"Error: {e}"