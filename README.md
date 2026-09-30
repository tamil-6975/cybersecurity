# 🔐 Password Strength Analyzer (Kali Linux Project)

## Overview
This project is a **Password Strength Analyzer** built in Python and tested on **Kali Linux**.  
It evaluates password robustness using:
- ✅ Regex pattern checks (length, uppercase, lowercase, digits, special characters)
- ✅ Common password detection with the **rockyou.txt** wordlist
- ✅ Human-readable strength levels (Very Weak → Very Strong)

This tool simulates real-world password auditing techniques used in penetration testing and cybersecurity.

---

##  Features
- Checks password length and complexity
- Detects if a password exists in leaked wordlists (`rockyou.txt`)
- Provides strength levels: Very Weak, Weak, Moderate, Strong, Very Strong
- Safe error handling if wordlist is missing

---

##  Installation & Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/password-analyzer.git
   cd password-analyzer
2. Run the script:
bash
python3 analyzer.py
3.Enter a password when prompted.
Example Output


---

## 🔍 Python Port Scanner — README

```markdown
# 🔍 Python Port Scanner (Kali Linux Project)

## 📖 Overview
This project is a **Port Scanner** built in Python and tested on **Kali Linux**.  
It scans a target IP address for open TCP ports, helping identify running services.  
This is a fundamental tool in penetration testing and network auditing.

---

## ⚙️ Features
- Scans first 1024 TCP ports
- Detects open ports using TCP connect
- Logs errors into a file (`errors.txt`) for review
- Lightweight and beginner-friendly

---

## 🛠️ Installation & Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/port-scanner.git
   cd password-analyzer
2. Run the script:
bash
python3 portscanner.py
Enter a target IP when prompted (e.g., 127.0.0.1).
3.Example Output
Code
Enter target IP: 127.0.0.1
Port 22: OPEN
Port 80: OPEN


