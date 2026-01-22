import random
import secrets
import string
import pyperclip

class PasswordGenerator:
    def __init__(self):
        self.character_sets = {
            'lowercase': string.ascii_lowercase,
            'uppercase': string.ascii_uppercase,
            'numbers': string.digits,
            'special': string.punctuation
        }
    
    def generate_password(self, length=12, include_uppercase=True, 
                         include_numbers=True, include_special=True):
        """Generate a secure random password with specified criteria"""
        
        # Build character pool based on user preferences
        char_pool = self.character_sets['lowercase']
        
        if include_uppercase:
            char_pool += self.character_sets['uppercase']
        if include_numbers:
            char_pool += self.character_sets['numbers']
        if include_special:
            char_pool += self.character_sets['special']
        
        # Validate we have at least one character type
        if not char_pool:
            return "Error: No character types selected"
        
        # Generate password using cryptographically secure random
        password = ''.join(secrets.choice(char_pool) for _ in range(length))
        
        return password
    
    def generate_multiple(self, count=5, **kwargs):
        """Generate multiple passwords with same criteria"""
        return [self.generate_password(**kwargs) for _ in range(count)]
    
    def copy_to_clipboard(self, password):
        """Copy password to system clipboard"""
        try:
            pyperclip.copy(password)
            return True
        except:
            return False

def get_user_input():
    """Get password preferences from user"""
    print("Password Generator")
    print("-" * 30)
    
    try:
        length = int(input("Password length (8-64): "))
        length = max(8, min(64, length))
        
        include_uppercase = input("Include uppercase? (y/n): ").lower() == 'y'
        include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        include_special = input("Include special chars? (y/n): ").lower() == 'y'
        
        count = int(input("How many passwords to generate? (1-10): "))
        count = max(1, min(10, count))
        
        return length, include_uppercase, include_numbers, include_special, count
    except ValueError:
        print("Invalid input. Using default values.")
        return 12, True, True, True, 1

def main():
    """Main application function"""
    generator = PasswordGenerator()
    
    # Get user preferences
    length, include_uppercase, include_numbers, include_special, count = get_user_input()
    
    # Generate password(s)
    if count == 1:
        password = generator.generate_password(
            length=length,
            include_uppercase=include_uppercase,
            include_numbers=include_numbers,
            include_special=include_special
        )
        print(f"\nGenerated Password: {password}")
        
        # Copy to clipboard
        if generator.copy_to_clipboard(password):
            print("Password copied to clipboard!")
    else:
        passwords = generator.generate_multiple(
            count=count,
            length=length,
            include_uppercase=include_uppercase,
            include_numbers=include_numbers,
            include_special=include_special
        )
        print(f"\nGenerated {count} passwords:")
        for i, pwd in enumerate(passwords, 1):
            print(f"{i}. {pwd}")
    
    print("\n" + "=" * 30)
    print("Password generation complete!")

if __name__ == "__main__":
    main()
