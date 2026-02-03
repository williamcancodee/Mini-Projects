# Mini Projects

This folder contains a collection of small Python projects demonstrating various programming concepts and techniques. Each project is a standalone script with example usage.

## Projects

### 1. Caesar Cipher (`Caesar cipher.py`)

A program that implements the Caesar cipher technique for encrypting and decrypting text.

**Key Functions:**
- `caesar(text, shift, encrypt=True)`: Core function to shift letters in the text.
- `encrypt(text, shift)`: Encrypts the given text with the specified shift.
- `decrypt(text, shift)`: Decrypts the given text with the specified shift.

**Usage:**
- Shift must be an integer between 1 and 25.
- Example: Decrypts "Pbhentr vf sbhaq va hayvxryl cynprf." with shift 13 to reveal the original message.

### 2. Number Pattern Generator (`num_pattern_generator.py`)

A script that generates a simple number pattern based on an input integer.

**Key Function:**
- `number_pattern(n)`: Returns a string of numbers from 1 to n, separated by spaces.

**Usage:**
- Input must be a positive integer greater than 0.
- Example: `number_pattern(4)` returns "1 2 3 4".

### 3. RPG Game Character Creator (`rpg_game.py`)

An RPG character creation function that generates a character with stats and validates inputs.

**Key Function:**
- `create_character(name, strength, intelligence, charisma)`: Creates a character with the given name and stats.

**Features:**
- Name validation: Must be a non-empty string, no longer than 10 characters, no spaces.
- Stats: Each stat (strength, intelligence, charisma) must be an integer from 1 to 4, totaling exactly 7 points.
- Displays stats with visual bars (● for filled, ○ for empty).

**Usage:**
- Example: `create_character('ren', 4, 2, 1)` creates a valid character display.

### 4. PIN Extractor (`pin_extractor.py`)

A function that extracts "secret codes" from poems based on word lengths.

**Key Function:**
- `pin_extractor(poems)`: Takes a list of poems (strings) and returns a list of secret codes.

**How it Works:**
- For each poem, splits into lines and words.
- For each line index, appends the length of the word at that position (or '0' if no such word exists).
- Generates a numeric code per poem.

**Usage:**
- Input: List of poem strings.
- Example: Extracts codes from sample poems like "Stars and the moon shine in the sky...".
