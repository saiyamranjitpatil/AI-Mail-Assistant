import re


SCAM_KEYWORDS = [
    "lottery",
    "winner",
    "claim prize",
    "bank account",
    "pan card",
    "aadhaar",
    "otp",
    "verify account",
    "click here",
    "limited time",
    "urgent action",
    "congratulations",
    "gift card",
    "bitcoin",
    "crypto",
    "wire transfer",
    "payment failed",
    "account suspended",
    "tax refund",
    "free money"
]


def detect_scam(subject, body):
    """
    Detects possible phishing or scam emails.
    """

    text = f"{subject} {body}".lower()

    score = 0

    for keyword in SCAM_KEYWORDS:
        if re.search(rf"\b{re.escape(keyword)}\b", text):
            score += 1

    if score >= 3:
        return "HIGH"

    elif score >= 1:
        return "MEDIUM"

    return "LOW"