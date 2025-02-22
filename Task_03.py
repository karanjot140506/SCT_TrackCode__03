import re

def check_password_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))  # Fixed `re.match()`

    score = 0
    feedback = []

    # Criteria 1: Length
    if length >= 12:
        score += 1
    elif length >= 8:
        feedback.append("Consider using a longer password for better security.")

    # Criteria 2: Uppercase and lowercase
    if has_upper and has_lower:
        score += 1
    else:
        feedback.append("Mixing uppercase and lowercase letters enhances security.")

    # Criteria 3: Numbers
    if has_digit:
        score += 1
    else:
        feedback.append("Including numbers adds to the complexity of the password.")

    # Criteria 4: Special Characters
    if has_special:
        score += 1
    else:
        feedback.append("Special characters provide an extra layer of security.")

    if score >= 3:
        return "Strong password! Keep it safe."
    else:
        return "Weak password. " + " ".join(feedback)


if __name__ == "__main__":  # Fixed __name__ check
    print("Welcome to the Password Strength Checker!")
    print("Please enter your password below:")

    while True:
        password = input("> ")
        if password.lower() == 'exit':
            print("Exiting...")
            break
        strength_feedback = check_password_strength(password)
        print(strength_feedback)
