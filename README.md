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
Code
Enter a password: 123456
Strength: ⚠️ Common password found in rockyou.txt! Very Weak
Code
Enter a password: Garou@69
Strength: Very Strong
