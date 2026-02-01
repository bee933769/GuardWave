#!/usr/bin/env python3
import os, time, random
from datetime import datetime
from fpdf import FPDF

# ======================
# Config
# ======================
LOG_FILE = "../data/timeline.log"
PDF_FILE = "../data/timeline.pdf"

# Colors
RED='\033[1;31m'
GREEN='\033[1;32m'
YELLOW='\033[1;33m'
CYAN='\033[1;36m'
MAGENTA='\033[1;35m'
RESET='\033[0m'
CHECK = u'\u2714'
ALERT = u'\u26A0'

# Counters
counters = {"HIGH":0, "MEDIUM":0, "LOW":0}

# ======================
# Helpers
# ======================
def typewriter(text, delay=0.003):
    for c in text:
        print(c, end="", flush=True)
        time.sleep(delay)
    print()

def animate_ascii(text, delay=0.002):
    for line in text.splitlines():
        print(line)
        time.sleep(delay)

HEADER_ART = "="*60 + "\nGuardWave — Security Event Dashboard\nNO DAYS OFF. Signal over noise.\n" + "="*60
FOOTER_ART = "="*60 + "\nSession ended.\n" + "="*60

def sparkle_line():
    return "".join(random.choice(["■","□","▣","▦"]) for _ in range(30))

# ======================
# Banner & classify
# ======================
def banner():
    animate_ascii(HEADER_ART)
    typewriter(GREEN + "          NO DAYS OFF! Let's get to work..." + RESET)
    print(CYAN + "="*60 + RESET)

def classify(text):
    t = text.lower()
    if any(x in t for x in ["password reset", "new login", "signed in"]):
        return "ACCOUNT LOGIN ALERT", "MEDIUM", 2
    if any(x in t for x in ["verify your account", "urgent", "click here", "suspended"]):
        return "PHISHING / SCAM LIKELY", "HIGH", 3
    if any(x in t for x in ["permission", "access changed", "allowed"]):
        return "APP PERMISSION CHANGE", "MEDIUM", 2
    return "UNCLASSIFIED EVENT", "LOW", 1

def explain(category, risk):
    messages = {
        "ACCOUNT LOGIN ALERT": f"{YELLOW}{ALERT} Unexpected login detected. Secure account immediately!{RESET}",
        "PHISHING / SCAM LIKELY": f"{RED}{ALERT} Suspicious link/email. Do NOT click. Verify source.{RESET}",
        "APP PERMISSION CHANGE": f"{YELLOW}{ALERT} App permissions changed. Check/revoke access.{RESET}",
        "UNCLASSIFIED EVENT": f"{CYAN}{CHECK} No high-risk patterns. Stay alert.{RESET}"
    }
    return messages.get(category)

# ======================
# Logging & PDF
# ======================
def log_event(text, category, risk, score):
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    counters[risk] += 1
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} | {category} | {risk} | Score:{score} | {text}\n")

def export_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "GuardWave — Security Event Timeline", 0, 1, "C")
    pdf.set_font("Arial", "", 12)
    try:
        with open(LOG_FILE, "r") as f:
            for line in f:
                pdf.multi_cell(0, 8, line.strip())
        typewriter(f"{GREEN}[INFO]{RESET} Timeline exported to {PDF_FILE}")
    except FileNotFoundError:
        typewriter(f"{RED}[WARN]{RESET} No events logged yet. PDF not created.")
def show_timeline():
    print(CYAN + "\n--- Incident Timeline ---" + RESET)
    try:
        with open(LOG_FILE, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"{YELLOW}No events logged yet.{RESET}")

# ======================
# Dashboard
# ======================
def dashboard():
    print("\n" + CYAN + "="*40 + RESET)
    print(MAGENTA + "      CURRENT RISK DASHBOARD" + RESET)
    print(CYAN + "="*40 + RESET)
    print(f"{RED}HIGH:   {counters['HIGH']}{RESET}  | {YELLOW}MEDIUM: {counters['MEDIUM']}{RESET}  | {GREEN}LOW:    {counters['LOW']}{RESET}")
    print(CYAN + "="*40 + RESET)
    print("Sparkle: " + sparkle_line())
    print("Scan: " + sparkle_line())

# ======================
# Main loop
# ======================
def main():
    banner()
    while True:
        dashboard()
        typewriter("\nPaste alert (timeline/pdf/exit): ", 0.003)
        try:
            user_input = input().strip()
        except EOFError:
            typewriter(RED + "EOF reached. Exiting safely." + RESET)
            break

        if user_input.lower() == "exit":
            typewriter(GREEN + "Session ended. Stay aware." + RESET)
            animate_ascii(FOOTER_ART)
            break
        elif user_input.lower() == "timeline":
            show_timeline()
            continue
        elif user_input.lower() == "pdf":
            export_pdf()
            continue

        category, risk, score = classify(user_input)
        typewriter(f"\nCategory: {MAGENTA}{category}{RESET}")
        typewriter(explain(category, risk))
        log_event(user_input, category, risk, score)
        typewriter(f"{GREEN}[INFO]{RESET} Event logged.\n")

if __name__ == "__main__":
    main()
