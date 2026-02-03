def create_character(name, strength, intelligence, charisma):
    """
    Here we are creating a simple RPG character creation function.
    The program creates an RPG character with the given name and stats.
    
    Args:
        name: Character name (string)
        strength: Strength stat (integer, 1-4)
        intelligence: Intelligence stat (integer, 1-4)
        charisma: Charisma stat (integer, 1-4)
    
    Returns:
        A formatted string with character info or an error message
    """
    
    # Validate character name
    if not isinstance(name, str):
        return "The character name should be a string"
    
    if name == "":
        return "The character should have a name"
    
    if len(name) > 10:
        return "The character name is too long"
    
    if " " in name:
        return "The character name should not contain spaces"
    
    # Validate stats are integers
    if not all(isinstance(stat, int) for stat in [strength, intelligence, charisma]):
        return "All stats should be integers"
    
    # Validate stat ranges
    if any(stat < 1 for stat in [strength, intelligence, charisma]):
        return "All stats should be no less than 1"
    
    if any(stat > 4 for stat in [strength, intelligence, charisma]):
        return "All stats should be no more than 4"
    
    # Validate total points
    if strength + intelligence + charisma != 7:
        return "The character should start with 7 points"
    
    # Create the character display
    def create_stat_bar(value):
        """Creates a stat bar with filled and empty dots"""
        filled = "●" * value
        empty = "○" * (10 - value)
        return filled + empty
    
    result = f"{name}\n"
    result += f"STR {create_stat_bar(strength)}\n"
    result += f"INT {create_stat_bar(intelligence)}\n"
    result += f"CHA {create_stat_bar(charisma)}"
    
    return result


# Test the function
if __name__ == "__main__":
    # Valid character
    print(create_character('ren', 4, 2, 1))
    print("\n" + "="*30 + "\n")
    
    # Test some error cases
    print(create_character(123, 4, 2, 1))  # Not a string
    print(create_character('', 4, 2, 1))  # Empty name
    print(create_character('verylongname', 4, 2, 1))  # Too long
    print(create_character('ren solo', 4, 2, 1))  # Has spaces
    print(create_character('ren', 4.5, 2, 1))  # Not integers
    print(create_character('ren', 0, 4, 3))  # Less than 1
    print(create_character('ren', 5, 1, 1))  # More than 4
    print(create_character('ren', 3, 3, 3))  # Sum not equal to 7
    
    int(4)
    float()
