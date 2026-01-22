import random
import string

class PasswordGenerator:
    def __init__(self):
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.numbers = string.digits
        self.special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    def generate_password(self, password_length=12, include_uppercase=True, 
                         include_numbers=True, include_special=True):
        character_pool = self.lowercase
        
        if include_uppercase:
            character_pool += self.uppercase
        if include_numbers:
            character_pool += self.numbers
        if include_special:
            character_pool += self.special_chars
        
        if not character_pool:
            return "Error: No character types selected"
        
        generated_password = ''.join(random.choice(character_pool) 
                                   for _ in range(password_length))
        return generated_password
    
    def generate_multiple_passwords(self, count=5, password_length=12, 
                                   include_uppercase=True, include_numbers=True, 
                                   include_special=True):
        passwords = []
        for _ in range(count):
            password = self.generate_password(password_length, include_uppercase, 
                                            include_numbers, include_special)
            passwords.append(password)
        return passwords
