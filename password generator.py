import random
import string

def generate_password(length, use_numbers, use_symbols, use_uppercase, use_lowercase):
    password_chars = ''
    
    if use_numbers:
        password_chars += string.digits
    if use_symbols:
        password_chars += string.punctuation
    if use_uppercase:
        password_chars += string.ascii_uppercase
    if use_lowercase:
        password_chars += string.ascii_lowercase
    
    password = ''.join(random.choice(password_chars) for _ in range(length))
    
    # Ensure the password meets all the specified requirements
    while (not any(c.isdigit() for c in password) and use_numbers) or \
          (not any(c in string.punctuation for c in password) and use_symbols) or \
          (not any(c.isupper() for c in password) and use_uppercase) or \
          (not any(c.islower() for c in password) and use_lowercase):
        password = ''.join(random.choice(password_chars) for _ in range(length))
    
    return password

def main():
    print("Password Generator")
    print("------------------")
    
    length = int(input("Enter the password length: "))
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    
    password = generate_password(length, use_numbers, use_symbols, use_uppercase, use_lowercase)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()