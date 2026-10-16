# 🔐 Password Strength & Entropy Checker

A Python-based command-line security tool designed to evaluate password strength using cryptographic entropy calculations, complex character variety rules, and vulnerability filters against common weak passwords.

## ✨ Features
- **Entropy Analysis**: Calculates password randomness (in bits) to measure true resistance against brute-force attacks.
- **Complexity Checks**: Enforces length constraints, lowercase/uppercase letter distribution, numeric digits, and special characters.
- **Dictionary Filtering**: Automatically flags known common and vulnerable passwords (e.g., "password123", "admin", "qwerty").
- **Actionable Feedback**: Provides targeted recommendations to help users improve weak passwords.

## 🚀 Usage

You can run the script interactively or pass a password directly as a command-line argument:

### 1. Interactive Mode:
```bash
python checker.py

##sample output

==================================================
      🔐 Python Password Strength Checker
==================================================

--- Results ---
Strength Rating : Very Strong
Estimated Entropy: 124.54 bits

[+] Excellent! Your password meets strong security guidelines.
==================================================

This tool is intended strictly for educational purposes, security awareness, and personal password auditing.

Created by Eman Khan