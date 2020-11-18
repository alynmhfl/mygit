#function to compare the whether char use in word are the same
def are_anagrams(word1, word2):
    word1_sorted = sorted(word1)
    word2_sorted = sorted(word2)
    return word1_sorted == word2_sorted  #return true or false

print("Anagram Test")

#validate the input
valid_input_bool = False
while not valid_input_bool:
    try:
        two_words = input("Enter two space separeted words: ")
        word1, word2 = two_words.split() #split the input string into a list of words
        valid_input_bool = True
    except:
        print("Bad Input")

#print the result
if are_anagrams(word1, word2):
    print("The words {} and {} are anagrams.".format(word1,word2))
else:
    print("The words {} and {} are not anagrams.".format(word1,word2))
