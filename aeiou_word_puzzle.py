#find english word that has a,e,i,o,u in sequence

datafile=open('dictionary.txt','r')

def clean_word(word):
    return word.strip().lower()
    #return wordin lowercasestripped of whitespace

def get_vowel(word):
    vowel_str="aeiou"
    vowel_in_word=""
    for char in word:
        if char in vowel_str:
            vowel_in_word+=char
    return vowel_in_word
    #return vowels in string--includes repeats

print('find words containing vowels aeiou in that order')
for word in datafile:              #for each word in file
    word = clean_word(word)        #clean word
    if len(word)<=6:               #if word is too small, skit it
        continue
    vowel_str=get_vowel(word)      #get vowels in word
    if vowel_str=='aeiou':          #check if vowels are in this order
        print (word)



