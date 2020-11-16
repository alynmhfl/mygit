#this program will search throught a text file
#for a word containing vowel 'a', 'e', 'i', 'o', 'u'
#in sequence

import string
data_file = open ('dictionary.txt', 'r')

def clean_word(word):
    return word.strip().lower()

def get_vowels_in_word(word):
    vowel_str = 'aeiou'
    vowel_in_word = ''
    for char in word:
        if char in vowel_str:
            vowel_in_word += char
    return vowel_in_word

print("Find words containing vowels 'aeiou' in that order:")
for word in data_file:
    word = clean_word(word)
    if len(word) <= 6:
        continue
    vowel_str = get_vowels_in_word(word)
    if vowel_str == 'aeiou':
        print(word)
            
"""
output as 
sean@sean-HP:~/advprog/mygit$ /usr/bin/python3 /home/sean/advprog/mygit/201116_example_3.py
Find words containing vowels 'aeiou' in that order:
abstemious
abstemiously
abstentious
acheilous
acheirous
acleistous
aegiochus
affectious
aleikoum
anemious
annelidous
areithous
arsenious
arterious
bacterious
caesious
facetious
facetiously
fracedinous
half-serious
half-seriously
majestious
parecious
pareciously
tragedious
"""
