def are_anagrams(word1,word2):
	word1_sorted = sorted(word1)
	word2_sorted = sorted(word2)
	
	return word1_sorted == word2_sorted

print("anagram test")

valid_input_bool = False

while not valid_input_bool:
	try:

		two_words= input("enter 2 separated words: ")
		word1,word2 = two_words.split()
		
		valid_input_bool = True

	except ValueError:
		print("bad input!")

if are_anagrams(word1,word2):
	print("the words {} and {} are anagrams".format(word1,word2))
else:
	print("the words {} and {} are not anagrams".format(word1,word2))