import random_word
import art
import random

# Initialization of resources
total_word_letters = random.randint(5, 12)
word_to_guess = random_word.generate_word(total_word_letters)
the_hangman = art.hangman_guesses  # The art of hangman
display = ['_'] * len(word_to_guess)  # Initialize display with underscores
guessed_letters = []  # Keep track of guessed letters
tries = 0  # Number of tries used

print("Wellcome to Hangman! Hope you will enjoy this game!")
while tries < len(the_hangman):
    guess = input("Guess a letter: ").lower()  # Taking a guess from the user

    # Check if the letter has already been guessed
    if guess in guessed_letters:
        print("You already guessed that letter. Try another.")
        continue  # Skip to the next iteration of the loop

    guessed_letters.append(guess)  # Add the guessed letter to the list

    if guess in word_to_guess:
        # Update the display based on the guessed letter
        for i, letter in enumerate(word_to_guess):
            if letter == guess:
                display[i] = guess
    else:
        print("Sorry, try again.")
        print(the_hangman[tries])
        tries += 1

    print("Word:", ' '.join(display))  # Show the current state of the word

    # Check if the word has been completely guessed
    if '_' not in display:
        print("Congratulations! You've guessed the word.")
        break


# If the loop ends without guessing the word
if '_' in display:
    print("Sorry, you've used all your tries. The word was:", word_to_guess)
