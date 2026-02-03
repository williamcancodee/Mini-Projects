def pin_extractor(poems):
    #takes a list of poems (strings) and returns a list of secret codes
    secret_codes = []
    
    for poem in poems:
        # Extract the secret code from each poem
        secret_code = ''
        lines = poem.split('\n')
        for line_index, line in enumerate(lines):
            words = line.split()
            if len(words) > line_index:
                # Append the length of the word at the line index position
                secret_code += str(len(words[line_index]))
            else:
                # If there is no such word, append '0'
                secret_code += '0'
        secret_codes.append(secret_code)
        
    return secret_codes
poem = """Stars and the moon
shine in the sky
white and
until the end of the night"""

poem2 = 'The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow'
poem3 = 'There\nonce\nwas\na\ndragon'

print(pin_extractor([poem, poem2, poem3]))
