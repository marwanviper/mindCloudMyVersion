import random

"""
this module provides a function to generate a random password of specified length.
It uses a combination of uppercase, lowercase, digits, and special characters.
it have only one parameter to specify the length of the password, defaulting to 12 characters.
"""


def password_generator(length=12):
    """Generate a random password of specified length."""
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"  # Define the character set
    password = "".join(
        random.choice(characters) for _ in range(length)
    )  # pick random characters from the set and join them to form a password
    return password


if __name__ == "__main__":
    print("Generated Password:", password_generator(16))
    print("Generated Password:", password_generator())
