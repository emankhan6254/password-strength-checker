import re
import math
import sys

# A small list of common weak passwords to check against
COMMON_PASSWORDS = {
    "password", "123456", "12345678", "123456789", "qwerty", 
    "abc1234", "password1", "admin", "welcome", "letmein"
}

def calculate_entropy(password: str) -> float:
    """Calculates password entropy based on pool size and length."""
    charset_size = 0
    if re.search(r'[a-z]', password): charset_size += 26
    if re.search(r'[A-Z]', password): charset_size += 26
    if re.search(r'\d', password): charset_size += 10
    if re.search(r'[\W_]', password): charset_size += 32 # Special characters
    
    if charset_size == 0 or len(password) == 0:
        return 0.0
    
    # Entropy formula: length * log2(charset_size)
    entropy = len(password) * math.log2(charset_size)
    return round(entropy, 2)

def evaluate_password(password: str):
    feedback = []
    score = 0
    entropy = calculate_entropy(password)

    # 1. Check if it's in common dictionary
    if password.lower() in COMMON_PASSWORDS:
        feedback.append("Avoid common dictionary words and predictable patterns.")
        return "Very Weak", entropy, feedback

    # 2. Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
        feedback.append("Consider making the password at least 12 characters long.")
    else:
        feedback.append("Password is too short (minimum 8 characters recommended).")

    # 3. Character variety checks
    has_lower = bool(re.search(r'[a-z]', password))
    has_upper = bool(re.search(r'[A-Z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[\W_]', password))

    if has_lower: score += 1
    else: feedback.append("Add lowercase letters.")

    if has_upper: score += 1
    else: feedback.append("Add uppercase letters.")

    if has_digit: score += 1
    else: feedback.append("Add numbers.")

    if has_special: score += 1
    else: feedback.append("Add special characters (e.g., @, #, $, !).")

    # Determine Strength Label
    if score >= 6 and entropy > 60:
        strength = "Very Strong"
    elif score >= 5 and entropy > 45:
        strength = "Strong"
    elif score >= 3 and entropy > 25:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, entropy, feedback

def main():
    print("=" * 50)
    print("      🔐 Python Password Strength Checker")
    print("=" * 50)
    
    if len(sys.argv) > 1:
        password = sys.argv[1]
    else:
        password = input("Enter a password to test: ")

    strength, entropy, feedback = evaluate_password(password)

    print("\n--- Results ---")
    print(f"Strength Rating : {strength}")
    print(f"Estimated Entropy: {entropy} bits")
    
    if feedback:
        print("\nRecommendations for improvement:")
        for item in feedback:
            print(f" - {item}")
    else:
        print("\n[+] Excellent! Your password meets strong security guidelines.")
    print("=" * 50)

if __name__ == "__main__":
    main()