# Caesar Cipher program

import detect_language as detect
from art import logo

print(logo)
direction = input("Type 'encrypt' or 'decrypt': ").lower()
text = input("Type your message:\n")
shift = int(input("Type the shift number:\n"))


def caesar_cipher(input_text, input_shift, input_direction):
    alphabet = detect.detect_alphabet(input_text)
    if alphabet is None:
        print("Cannot determine the alphabet of the input text.")
        return input_text

    n = len(alphabet)  # Using full length of alphabet
    encrypted_text = ""
    new_index = 0
    for letter in input_text:
        if letter in alphabet:
            index = alphabet.index(letter)
            if input_direction == 'encrypt':
                new_index = (index + input_shift) % n
            elif input_direction == 'decrypt':
                new_index = (index - input_shift + n) % n
            new_letter = alphabet[new_index]
            encrypted_text += new_letter
        else:
            encrypted_text += letter

    return encrypted_text


# Use the function
result = caesar_cipher(text, shift, direction)
print(f"The result is: {result}")
