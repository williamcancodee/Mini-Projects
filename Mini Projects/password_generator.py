import random
import string

def generate_password(length=12, include_uppercase=True, include_lowercase=True, include_numbers=True, include_symbols=True):
    """
    Generates a random password based on specified criteria.

    Args:
        length (int): The length of the password (default 12, min 4, max 50).
        include_uppercase (bool): Include uppercase letters (default True).
        include_lowercase (bool): Include lowercase letters (default True).
        include_numbers (bool): Include numbers (default True).
        include_symbols (bool): Include symbols (default True).

    Returns:
        str: The generated password or an error message.
    """

    # Validate length
    if not isinstance(length, int) or length < 4 or length > 50:
        return "Password length must be an integer between 4 and 50."

    # Ensure at least one character type is selected
    if not any([include_uppercase, include_lowercase, include_numbers, include_symbols]):
        return "At least one character type must be included."

    # Build the character pool
    characters = ""
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Test the function
if __name__ == "__main__":
    print("Default password:", generate_password())
    print("Short password:", generate_password(8))
    print("Numbers only:", generate_password(10, include_uppercase=False, include_lowercase=False, include_symbols=False))
    print("Error - no types:", generate_password(include_uppercase=False, include_lowercase=False, include_numbers=False, include_symbols=False))
    print("Error - invalid length:", generate_password(3))
