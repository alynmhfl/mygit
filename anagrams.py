def anagrams(word1, word2):  #function returned true or false
    w_sort1=sorted(word1) 
    w_sort2=sorted(word2)
    return w_sort1==w_sort2  

print('Anagram test')



   
two_words=input('Enter two spaces seperated words: ')
word1,word2= two_words.split()  #split input string into list
     
                   
        


if anagrams(word1,word2):  
    print('the words are anagrams.')  
else:
    print('the words are not anagrams.')