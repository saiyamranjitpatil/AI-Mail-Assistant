import re
import dateparser


def detect_deadline(text):
    """
    Detect deadlines mentioned in an email.
    """

    if not text:
        return "No deadline"

    patterns = [
        r"before\s+([^.!,\n]+)",
        r"by\s+([^.!,\n]+)",
        r"within\s+([^.!,\n]+)",
        r"on\s+([^.!,\n]+)"
    ]

    for pattern in patterns:

        matches = re.findall(pattern, text, flags=re.IGNORECASE)

        for match in matches:

            parsed = dateparser.parse(match)

            if parsed:
                return parsed.strftime("%d %b %Y %I:%M %p")

            return match.strip()

    return "No deadline"