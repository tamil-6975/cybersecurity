import re

def check_strength(password):
    score = 0
 # Check if password is common
    try:
        with open("/usr/share/wordlists/rockyou.txt", "r", encoding="latin-1") as f:
            common = f.read().splitlines()
        if password in common:
            return "⚠️ Common password found in rockyou.txt! Very Weak"
    except FileNotFoundError:
        print("Wordlist not found. Skipping common password check.")
    if len(password) >= 8:
       score += 1
    if re.search(r"[A-Z]", password):
       score += 1
    if re.search(r"[a-z]", password):
       score += 1
    if re.search(r"[0-9]", password):
       score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    levels = {
        1: "very weak",
        2: "weak",
        3: "Moderate",
        4: "Strong",
        5: "Very strong"
    }
    return levels.get(score, "very weak")

password = input("Enter a password:")
print("Strength:", check_strength(password))
