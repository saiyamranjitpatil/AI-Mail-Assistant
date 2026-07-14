import time

from gmail_reader import authenticate_gmail, get_unread_emails
from summarizer import summarize_email

from utils.reading_time import estimate_reading_time
from utils.deadline_detector import detect_deadline
from utils.priority_rules import detect_priority
from utils.email_cleaner import clean_email
from utils.scam_detector import detect_scam


def main():

    start_time = time.time()

    print("\nSaiyam AI Mail Assistant\n")
    print("Checking Gmail...\n")

    service = authenticate_gmail()

    emails = get_unread_emails(service)

    print(f"{len(emails)} Emails Found\n")

    print("=" * 90)

    for email in emails:

        original_body = email["body"]

        cleaned_body = clean_email(original_body)

        reading_time = estimate_reading_time(cleaned_body)

        deadline = detect_deadline(cleaned_body)

        priority = detect_priority(
            email["subject"],
            cleaned_body
        )

        scam_risk = detect_scam(
            email["subject"],
            cleaned_body
        )

        print(f"\nFrom         : {email['sender']}")
        print(f"Subject      : {email['subject']}")
        print(f"Priority     : {priority}")
        print(f"Scam Risk    : {scam_risk}")
        print(f"Reading Time : {reading_time}")
        print(f"Deadline     : {deadline}")

        print("\nSummarizing...\n")

        summary = summarize_email(
            cleaned_body,
            priority
        )

        print(summary)

        print("\n" + "=" * 90)

    total_time = time.time() - start_time

    print(f"\nCompleted in {total_time:.2f} seconds")


if __name__ == "__main__":
    main()