data_file = open("dictionary.txt",'r')
def clean_word(word):
    return word.strip().lower()

def get_vowels_in_word(word):

    vowel_str = "aeiou"
    vowel_in_word = ""
    for char in word:
        if char in vowel_str:
            vowel_in_word += char
    return vowel_in_word

#main

print("Find words containing vowels 'aeiou' in that order:")
for word in data_file:
    word = clean_word(word)
    if len(word) <= 6:
        continue
    vowel_str = get_vowels_in_word(word)
    if vowel_str == 'aeiou':
        print(word)