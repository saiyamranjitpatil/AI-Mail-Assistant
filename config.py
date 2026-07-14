"""
Application configuration.
"""

# Gmail API permissions
SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly"
]

# Number of unread emails to fetch
MAX_EMAILS = 10

# Local LLM configuration
OLLAMA_MODEL = "qwen2.5:3b"
OLLAMA_URL = "http://localhost:11434/api/generate"