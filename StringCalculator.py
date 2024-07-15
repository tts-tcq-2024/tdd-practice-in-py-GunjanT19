# soundex.py

# Soundex mapping for each letter from 'A' to 'Z'
soundex_mapping = [
    0, 1, 2, 3, 0, 1, 2, 0, 0, 2,
    2, 4, 5, 5, 0, 1, 2, 6, 2, 3,
    0, 1, 0, 2, 0, 2
]

# Function: get_soundex_code
# Returns the Soundex code for a given character 'c'
def get_soundex_code(c):
    c = c.upper()  # Convert character to uppercase
    if not 'A' <= c <= 'Z':
        return '0'  # Return '0' for non-alphabet characters
    return str(soundex_mapping[ord(c) - ord('A')])

# Function: append_soundex_code
# Appends a Soundex code 'code' to the 'soundex' string if it's not '0' and not the same as the last appended code
def append_soundex_code(code, soundex, sIndex):
    if code != '0' and code != soundex[sIndex - 1]:
        soundex.append(code)  # Append the code to soundex

# Function: finalize_soundex
# Finalizes the 'soundex' list by padding with '0's until it reaches a length of 4 characters
def finalize_soundex(soundex):
    while len(soundex) < 4:
        soundex.append('0')  # Fill remaining characters with '0'

# Function: generate_soundex
# Generates the Soundex code for a given 'name' and returns it as a string
def generate_soundex(name):
    soundex = [name[0].upper()]  # Store the uppercase first letter of 'name' in 'soundex'
    sIndex = 1  # Initialize index for 'soundex'

    for i in range(1, len(name)):
        code = get_soundex_code(name[i])  # Get Soundex code for current character in 'name'
        append_soundex_code(code, soundex, sIndex)  # Append code to 'soundex' if necessary
        sIndex += 1

        if sIndex >= 4:
            break
    
    finalize_soundex(soundex)  # Finalize 'soundex' to ensure it is exactly 4 characters long
    return ''.join(soundex)  # Convert list to string and return the final Soundex code

# Example usage:
if __name__ == '__main__':
    name = "Johnson"
    print(f"Soundex code for '{name}' is '{generate_soundex(name)}'")
