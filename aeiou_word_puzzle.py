#find english word that has a,e,i,o,u in sequence

datafile=open('dictionary.txt','r')

def clean_word(word):
    return word.strip().lower()

def get_vowel(word):
    vowel_str="aeiou"
    vowel_in_word=""
    for char in word:
        if char in vowel_str:
            vowel_in_word+=char
    return vowel_in_word

print('find words containing vowels aeiou in that order')
for word in datafile:
    word = clean_word(word)
    if len(word)<=6:
        continue
    vowel_str=get_vowel(word)
    if vowel_str=='aeiou':
        print (word)



