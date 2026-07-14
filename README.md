# AI Mail Assistant

An AI-powered Gmail productivity assistant built with Python, the Gmail API, and a locally hosted Large Language Model (Qwen2.5 via Ollama). The application reads unread Gmail messages, performs intelligent preprocessing in Python, and generates executive-style summaries with actionable insights, while minimizing unnecessary LLM usage.

---

## Table of Contents

- [Overview](#overview)
- [Why This Project?](#why-this-project)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Architecture](#project-architecture)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Gmail API Setup](#gmail-api-setup)
- [Running the Project](#running-the-project)
- [Sample Output](#sample-output)
- [Future Improvements](#future-improvements)
- [Key Skills Demonstrated](#key-skills-demonstrated)
- [License](#license)

---

## Overview

Manually triaging a crowded inbox is slow and repetitive. AI Mail Assistant automates the first pass: it connects to Gmail, pulls in unread messages, cleans and analyzes them using deterministic Python logic, and only invokes the local LLM when genuine summarization is required. The result is a concise, structured briefing for each email, covering priority, deadlines, phishing risk, and a short executive summary with a clear action item.

By keeping preprocessing rule-based and reserving the LLM strictly for summarization, the application stays fast, predictable, and fully local, with no email content ever leaving the machine.

---

## Why This Project?

Most AI email assistants rely heavily on LLMs for every task, increasing latency and computation.

This project takes a hybrid approach by combining deterministic Python logic with a local LLM. Python handles structured tasks such as priority detection, deadline extraction, scam detection, and email cleaning, while the LLM is reserved solely for contextual summarization.

This design improves efficiency, reduces unnecessary inference, and demonstrates how traditional software engineering and AI can work together.

---

## Features

- Gmail OAuth 2.0 authentication
- Gmail API integration for reading unread messages
- Local AI summarization using Ollama (Qwen2.5)
- Reading time estimation
- Rule-based priority detection
- Deadline detection and parsing
- Email cleaning and noise removal
- Scam and phishing risk detection
- Executive-style email summaries with action items

---

## Tech Stack

| Component        | Technology            |
|-------------------|------------------------|
| Language          | Python 3.11            |
| Email Access      | Gmail API               |
| Authentication    | Google OAuth 2.0        |
| LLM Runtime       | Ollama                  |
| Model             | Qwen2.5                 |
| HTTP Client       | Requests                |
| Date Parsing      | Dateparser               |

---

## Project Architecture

```
Unread Email
    |
    v
Email Cleaner
    |
    v
Reading Time
    |
    v
Deadline Detection
    |
    v
Priority Rules
    |
    v
Scam Detection
    |
    v
Qwen2.5 (Ollama)
    |
    v
Executive Summary
```

The pipeline is intentionally layered so that only the final summarization step depends on the LLM. Every stage before it (cleaning, reading time, deadline detection, priority rules, and scam detection) runs on deterministic Python logic, keeping the system fast and predictable.

---

## Project Structure

```
AI-Mail-Assistant/
├── main.py
├── config.py
├── gmail_reader.py
├── email_processor.py
├── summarizer.py
├── requirements.txt
├── README.md
├── .gitignore
└── utils/
    ├── __init__.py
    ├── reading_time.py
    ├── deadline_detector.py
    ├── priority_rules.py
    ├── email_cleaner.py
    └── scam_detector.py
```

---

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/YOUR_USERNAME/AI-Mail-Assistant.git
```

**2. Move into the project directory**

```bash
cd AI-Mail-Assistant
```

**3. Create a virtual environment**

```bash
python -m venv venv
```

**4. Activate the environment**

macOS / Linux
```bash
source venv/bin/activate
```

Windows
```bash
venv\Scripts\activate
```

**5. Install dependencies**

```bash
pip install -r requirements.txt
```

---

## Gmail API Setup

1. Create a project in the Google Cloud Console.
2. Enable the Gmail API for that project.
3. Configure the OAuth consent screen.
4. Create OAuth credentials for a Desktop application.
5. Download the generated credentials file.
6. Rename the file to `credentials.json`.
7. Place it in the project root directory.

On the first successful login, the application automatically generates a `token.json` file to persist the authenticated session.

> **Note:** `credentials.json` and `token.json` are intentionally excluded from version control via `.gitignore`, as they contain sensitive authentication information and must never be committed to a public repository.

---

## Running the Project

```bash
python main.py
```

On first run, a browser window will open to complete the Google OAuth flow. Subsequent runs will reuse the stored token until it expires.

---

## Sample Output

```
From         : HR Team
Subject      : Final Interview Invitation
Priority     : HIGH
Scam Risk    : LOW
Reading Time : Less than 1 min
Deadline     : Tomorrow 8:00 PM

Summary
- Final interview scheduled.
- Confirmation required before tomorrow.
- Meeting details will be shared after confirmation.

Action Required
Confirm interview availability.
```

---

## Future Improvements

- Attachment detection and summarization
- AI-generated reply drafts
- Smart email caching to reduce redundant API calls
- Desktop notifications for high-priority emails
- Daily executive dashboard view
- Web-based interface

---

## Key Skills Demonstrated

Building this project provided hands-on experience with:

- OAuth 2.0 authentication flows
- Gmail API integration
- Prompt engineering for local LLMs
- Local LLM deployment and inference using Ollama
- Python automation and pipeline design
- Modular software architecture
- Rule-based NLP preprocessing
- Third-party API integration

---

## License

This project is released under the MIT License.
