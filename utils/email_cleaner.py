import re


def clean_email(text):
    """
    Cleans the email before sending it to the LLM.
    """

    if not text:
        return ""

    # Remove URLs
    text = re.sub(r"http\S+|www\S+", "", text)

    # Remove email addresses
    text = re.sub(r"\S+@\S+", "", text)

    # Remove common newsletter/footer phrases
    footer_patterns = [
        r"unsubscribe.*",
        r"privacy policy.*",
        r"terms of service.*",
        r"view in browser.*",
        r"manage preferences.*",
        r"all rights reserved.*",
        r"copyright.*",
        r"follow us.*"
    ]

    for pattern in footer_patterns:
        text = re.sub(
            pattern,
            "",
            text,
            flags=re.IGNORECASE | re.DOTALL
        )

    # Replace multiple blank lines with one
    text = re.sub(r"\n\s*\n+", "\n\n", text)

    # Replace multiple spaces
    text = re.sub(r"[ \t]+", " ", text)

    return text.strip()