# Return True, if words are anagrams.
# Sort the characters of the words.

def are_anagrams(word1,word2):
  word1_sorted = sorted(word1)		# Sorted returns a sorted list
  word2_sorted = sorted(word2)
  return word1_sorted == word2_sorted	# Check that the sortedwords are identical

print("Anagram test")

# Input two words.

two_words = input("Enter two space separated words: ")
word1,word2 = two_words.split()		# Split into a list of words

if are_anagrams(word1,word2):		# Return True or False
  print("The words are anagrams.")
else:
  print("the words are not anagrams.")

