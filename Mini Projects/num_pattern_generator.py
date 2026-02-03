def number_pattern(n):
    # User Story 6: Check for non-integers first
    if not isinstance(n, int):
        return "Argument must be an integer value."
    
    # User Story 7: Then check if the integer is positive
    elif n <= 0:
        return "Argument must be an integer greater than 0."
        
    # User Stories 3-5: Logic for the pattern
    result = ""
    for number in range(1, n + 1):
        result += str(number) + " "
        
    return result.strip()

# Test the function
print(number_pattern(4))