# open file named "dictionary.txt" for reading('r')
data_file = open("dictionary.txt", "r")

def clean_word(word):
    """Return vowels lowercase in stripped of whitespace"""
    return word.strip().lower()

def get_vowels_in_word(word):
    """Return vowels in string word-include repeats."""
    vowel_str = "aeiou"
    vowel_in_word = ""
    for char in word:
        if char in vowel_str:
            vowel_in_word += char
    return vowel_in_word

# main program

print("Find word containing vowels 'aeiou' in that order:")
for word in data_file:    # for each word in the file
    word = clean_word(word)  # clean the word
    if len(word) <= 6:  # if word is too small. skip it
        continue
    vowel_str = get_vowels_in_word(word)  # get vowels in word
    if vowel_str == 'aeiou':  # check if you have exactly vowel in order
        print(word)