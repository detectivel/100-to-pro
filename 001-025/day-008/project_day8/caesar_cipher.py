# Caesar Cipher program

print("Welcome to the Caesar Cipher encryption Program!")

# Generate uppercase letters (A-Z)
uppercase_letters = [chr(i) for i in range(65, 91)]

# Generate lowercase letters (a-z)
lowercase_letters = [chr(i) for i in range(97, 123)]

# Generate numbers (0-9) as characters
number_characters = [chr(i) for i in range(48, 58)]

# Optionally, combine both lists if you want all letters in one list
all_letters = uppercase_letters + lowercase_letters

direction = input("Type 'encrypt' or 'decrypt'")
text = input("Type your message:\n")
shift = int(input("Type the shift number:\n"))


def caesar_cipher(input_text, input_shift, input_direction):
    encrypted_text = ""
    for letter in input_text:
        if letter in uppercase_letters:
            alphabet = uppercase_letters
        elif letter in lowercase_letters:
            alphabet = lowercase_letters
        else:
            # If the character is not in the lists, add it directly to the encrypted_text.
            encrypted_text += letter
            continue
        # Find the new position with wrapping
        position = alphabet.index(letter)
        if input_direction == 'encrypt':
            new_position = (position + input_shift) % len(alphabet)
        elif input_direction == 'decrypt':
            new_position = (position - input_shift) % len(alphabet)
        else:
            return "Invalid direction. Choose 'encrypt' or 'decrypt'."

        new_letter = alphabet[new_position]
        encrypted_text += new_letter

    return encrypted_text


# Use the function
result = caesar_cipher(text, shift, direction)
print(f"The result is: {result}")