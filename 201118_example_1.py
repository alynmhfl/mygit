def are_anagrams(word1,word2):
    word1_sorted = sorted(word1)
    word2_sorted = sorted(word2)

    return word1_sorted == word2_sorted

if __name__ == '__main__':
    print("Anagram Test")
    two_words = input ("Enter two spaces seperated words: ")
    word1,word2 = two_words.split()

    if are_anagrams(word1,word2):
        print("The words are anagrams.")
    else:
        print("The words are not anagrams.")
