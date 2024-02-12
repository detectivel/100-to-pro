import languages as lang


def detect_alphabet(input_text):
    for char in input_text:
        if char.isalpha():
            # English
            if ord('A') <= ord(char) <= ord('Z') or ord('a') <= ord(char) <= ord('z'):
                return lang.eng_alphabet
            # Russian
            elif ord('А') <= ord(char) <= ord('я') or char in 'Ёё':
                return lang.rus_alphabet
            # German
            elif char in 'ÄÖÜäöüß':
                return lang.german_alphabet
            # French
            elif char in 'ÀÂÆÇÉÈÊËÎÏÔŒÙÛÜÝàâæçéèêëîïôœùûüýÿ':
                return lang.french_alphabet
            # Spanish
            elif char in 'Ññ':
                return lang.spanish_alphabet
    return None
