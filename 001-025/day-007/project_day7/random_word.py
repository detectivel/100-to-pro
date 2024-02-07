from faker import Faker

fake = Faker()


# Function to generate a word with a minimum length of 7 letters

def generate_word(letters):
    while True:
        word = fake.word()
        if len(word) == letters:
            return word
