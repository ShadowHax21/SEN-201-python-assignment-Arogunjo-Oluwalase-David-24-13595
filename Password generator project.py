import secrets
import string
import pyperclip
import sys

def generate_password(length=16, use_upper=True, use_lower=True, use_digits=True, use_special=True):
    """Generate a secure random password with specified character types"""
    
    # Character sets
    upper = string.ascii_uppercase if use_upper else ''
    lower = string.ascii_lowercase if use_lower else ''
    digits = string.digits if use_digits else ''
    special = string.punctuation if use_special else ''
    
    # Combine selected character sets
    all_characters = upper + lower + digits + special
    
    if not all_characters:
        return "Error: No character types selected"
    
    # Ensure at least one character from each selected type
    password = []
    if use_upper:
        password.append(secrets.choice(upper))
    if use_lower:
        password.append(secrets.choice(lower))
    if use_digits:
        password.append(secrets.choice(digits))
    if use_special:
        password.append(secrets.choice(special))
    
    # Fill the rest with random characters from all sets
    remaining_length = length - len(password)
    password.extend(secrets.choice(all_characters) for _ in range(remaining_length))
    
    # Shuffle to avoid predictable patterns
    secrets.SystemRandom().shuffle(password)
    
    return ''.join(password)

def main():
    print("=" * 50)
    print("Secure Password Generator")
    print("=" * 50)
    
    try:
        # Get password count
        while True:
            try:
                count = int(input("How many passwords to generate? (1-20): "))
                if 1 <= count <= 20:
                    break
                print("Please enter a number between 1 and 20")
            except ValueError:
                print("Please enter a valid number")
        
        # Get password length
        while True:
            try:
                length = int(input("Password length? (8-64): "))
                if 8 <= length <= 64:
                    break
                print("Please enter a number between 8 and 64")
            except ValueError:
                print("Please enter a valid number")
        
        # Character type preferences
        print("\nCharacter types to include:")
        use_upper = input("Uppercase letters? (Y/n): ").lower() != 'n'
        use_lower = input("Lowercase letters? (Y/n): ").lower() != 'n'
        use_digits = input("Digits? (Y/n): ").lower() != 'n'
        use_special = input("Special characters? (Y/n): ").lower() != 'n'
        
        print("\n" + "=" * 50)
        print(f"Generating {count} password(s)...")
        print("=" * 50)
        
        # Generate passwords
        passwords = []
        for i in range(count):
            password = generate_password(length, use_upper, use_lower, use_digits, use_special)
            passwords.append(password)
            print(f"{i+1:2}. {password}")
        
        # Clipboard support
        if passwords:
            copy_choice = input(f"\nCopy password #1 to clipboard? (y/N): ").lower()
            if copy_choice == 'y':
                pyperclip.copy(passwords[0])
                print("✓ Password copied to clipboard!")
            
            # Option to save all passwords to file
            save_choice = input("\nSave all passwords to file? (y/N): ").lower()
            if save_choice == 'y':
                filename = input("Filename (default: passwords.txt): ") or "passwords.txt"
                with open(filename, 'w') as f:
                    for i, pwd in enumerate(passwords, 1):
                        f.write(f"{i}. {pwd}\n")
                print(f"✓ Passwords saved to {filename}")
        
    except KeyboardInterrupt:
        print("\n\nOperation cancelled.")
        sys.exit(0)
    except Exception as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    # Install pyperclip if not available
    try:
        import pyperclip
    except ImportError:
        print("Installing required module: pyperclip")
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyperclip"])
        import pyperclip
    
    main()
