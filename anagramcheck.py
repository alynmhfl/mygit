def anagrams(word1, word2):
    sort1=sorted(word1)  #sorted returns a sorted list
    sort2=sorted(word2)
    return sort1==sort2  #checks both words are identical or not

print('anagram test')

valid_input_bool=False
while not valid_input_bool:
    try:
        twowords=input('enter two space separated words: ')
        word1,word2= twowords.split()  #split input string into list
        valid_input_bool=True
    except ValueError:                #checking input error
        print('bad input')


if anagrams(word1,word2):  #function returned true or false
    print('the words {} and {} are anagrams.'.format(word1,word2))  
else:
    print('the words {} and {} are not anagrams.'.format(word1,word2))