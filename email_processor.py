import base64


def extract_email_body(payload):
    """
    Extracts the plain text body from a Gmail message payload.
    Returns a clean string.
    """

    body = ""

    # Simple emails
    if "parts" not in payload:

        data = payload["body"].get("data")

        if data:

            body = base64.urlsafe_b64decode(
                data.encode("UTF-8")
            ).decode("utf-8", errors="ignore")

    else:

        # Multipart emails
        for part in payload["parts"]:

            if part["mimeType"] == "text/plain":

                data = part["body"].get("data")

                if data:

                    body = base64.urlsafe_b64decode(
                        data.encode("UTF-8")
                    ).decode("utf-8", errors="ignore")

                    break

    return body.strip()