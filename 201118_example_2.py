# Return True, if words are anagrams.
# Sort the characters of the words.

def are_anagrams(word1,word2):
  word1_sorted = sorted(word1)		# Sorted returns a sorted list
  word2_sorted = sorted(word2)
  return word1_sorted == word2_sorted	# Check that the sortedwords are identical

print("Anagram test")

# Input two words, checking for errors now.

valid_input_bool = False
while not valid_input_bool:
  try:
    two_words = input("Enter two space separated words: ")
    word1,word2 = two_words.split()		# Split input string into a list of words
    valid_input_bool = True

  except ValueError:
    print("Bad Input.")

if are_anagrams(word1,word2):			# Function returned True or False
  print("The words {} and {} are anagrams.".format(word1,word2))
else:
  print("the words {} and {} are not anagrams.".format(word1,word2))
