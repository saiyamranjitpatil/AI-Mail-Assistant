import re


HIGH_PRIORITY = [
    "interview",
    "deadline",
    "urgent",
    "security",
    "payment",
    "invoice",
    "meeting",
    "offer",
    "flight",
    "cancelled",
    "verification",
    "otp"
]

MEDIUM_PRIORITY = [
    "assignment",
    "project",
    "update",
    "reminder",
    "schedule",
    "submission",
    "event"
]


def detect_priority(subject, body):

    text = f"{subject} {body}".lower()

    for word in HIGH_PRIORITY:
        if re.search(rf"\b{re.escape(word)}\b", text):
            return "HIGH"

    for word in MEDIUM_PRIORITY:
        if re.search(rf"\b{re.escape(word)}\b", text):
            return "MEDIUM"

    return "LOW"