from faker import Faker
import random
import string
import time

fake = Faker()

class Helper:
    def generate_user_data(self):
        return {
            "email": self.generate_unique_email(),
            "password": self.generate_valid_password(),
            "name": fake.first_name()
        }
    
    def generate_unique_email(self):
        """Генерация уникального email с timestamp"""
        timestamp = int(time.time() * 1000)
        return f"test_user_{timestamp}@example.com"
    
    def generate_valid_password(self):
        """Генерация валидного пароля"""
        length = random.randint(8, 12)
        letters = string.ascii_letters
        digits = string.digits
        password = ''.join(random.choice(letters + digits) for _ in range(length))
        
        # Убедимся что есть хотя бы одна цифра и одна буква
        if not any(char.isdigit() for char in password):
            password = password[:-1] + random.choice(digits)
        if not any(char.isalpha() for char in password):
            password = password[:-1] + random.choice(letters)
            
        return password
    
    def get_credentials(self, user_data):
        return {
            "email": user_data["email"],
            "password": user_data["password"]
        }
    
    def generate_user_without_email(self):
        return {
            "password": self.generate_valid_password(),
            "name": fake.first_name()
        }
    
    def generate_user_without_password(self):
        return {
            "email": self.generate_unique_email(),
            "name": fake.first_name()
        }
    
    def generate_user_without_name(self):
        return {
            "email": self.generate_unique_email(),
            "password": self.generate_valid_password()
        }
    
    def generate_invalid_credentials(self):
        return {
            "email": "invalid@example.com",
            "password": "invalid_password"
        }