def generate_alphabet(start, end):
    return ''.join([chr(i) for i in range(start, end + 1)])


# English alphabet
eng_alphabet = generate_alphabet(65, 90) + generate_alphabet(97, 122)

# Russian alphabet
rus_alphabet = generate_alphabet(1040, 1071) + 'Ё' + generate_alphabet(1072, 1103) + 'ё'

# German alphabet (adding letters ß, а and others)
german_alphabet = eng_alphabet + 'ÄÖÜäöüß'

# French alphabet (including с with diacritics characters)
french_alphabet = eng_alphabet + 'ÀÂÆÇÉÈÊËÎÏÔŒÙÛÜÝàâæçéèêëîïôœùûüýÿ'

# Spanish alphabet (adding Ññ and using the same base letters as in english)
spanish_alphabet = eng_alphabet + 'Ññ'

# Hebrew
hebrew_alphabet = generate_alphabet(1488, 1514)