import random
import string

def generate_password(length):
    # Define character sets for different types of characters
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Ensure the password length is at least 8 characters
    if length < 8:
        print("Password length must be at least 8 characters.")
        return None

    # Generate the password
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

# Get the desired password length from the user
try:
    password_length = int(input("Enter the desired password length: "))
    password = generate_password(password_length)
    if password:
        print("Generated Password:", password)
except ValueError:
    print("Invalid input. Please enter a valid number for the password length.")
