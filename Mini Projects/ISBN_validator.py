def validate_isbn(isbn, length):
    # Fix TypeError: len() takes exactly one argument
    if len(isbn) != length:
        print(f'ISBN-{length} code should be {length} digits long.')
        return
    
    # Fix Off-by-one error: Slice up to the last digit (excluding it)
    main_digits = isbn[:-1]
    
    # Fix IndexError: Access the last character correctly
    given_check_digit = isbn[-1]
    
    # Fix ValueError: Handle non-numeric characters in the ISBN
    try:
        main_digits_list = [int(digit) for digit in main_digits]
    except ValueError:
        print("Invalid character was found.")
        return

    # Calculate the check digit from other digits
    if length == 10:
        expected_check_digit = calculate_check_digit_10(main_digits_list)
    else:
        expected_check_digit = calculate_check_digit_13(main_digits_list)
    
    # Check if the given check digit matches with the calculated check digit
    if given_check_digit == expected_check_digit:
        print('Valid ISBN Code.')
    else:
        print('Invalid ISBN Code.')

def calculate_check_digit_10(main_digits_list):
    digits_sum = 0
    # Multiply each of the first 9 digits by its corresponding weight (10 to 2)
    for index, digit in enumerate(main_digits_list):
        digits_sum += digit * (10 - index)
    
    # Find the remainder of dividing the sum by 11, then subtract it from 11
    result = 11 - digits_sum % 11
    
    if result == 11:
        expected_check_digit = '0'
    elif result == 10:
        expected_check_digit = 'X'
    else:
        expected_check_digit = str(result)
    
    return expected_check_digit

def calculate_check_digit_13(main_digits_list):
    digits_sum = 0
    # Multiply each of the first 12 digits by 1 and 3 alternately
    for index, digit in enumerate(main_digits_list):
        if index % 2 == 0:
            digits_sum += digit * 1
        else:
            digits_sum += digit * 3
    
    # Find the remainder of dividing the sum by 10, then subtract it from 10
    result = 10 - digits_sum % 10
    
    if result == 10:
        expected_check_digit = '0'
    else:
        expected_check_digit = str(result)
    
    return expected_check_digit

def main():
    user_input = input('Enter ISBN and length: ')
    
    values = user_input.split(',')
    
    # Handle IndexError if the user did not enter a comma
    try:
        isbn = values[0].strip()
        length_input = values[1].strip()
    except IndexError:
        print('Enter comma-separated values.')
        return

    # Handle ValueError if the length is not a number
    try:
        length = int(length_input)
    except ValueError:
        print('Length must be a number.')
        return

    if length == 10 or length == 13:
        validate_isbn(isbn, length)
    else:
        print('Length should be 10 or 13.')


main()