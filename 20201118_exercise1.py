def are_anagrams(word1, word2):
	word1_sorted = sorted(word1)		#sorted returns a sorted list
	word2_sorted = sorted(word2)
	return word1_sorted == word2_sorted

print ("ANAGRAM TEST")

valid_input_bool = False
while not valid_input_bool:
	try:
		two_words = input ("Enter two space separated words: ")
		word1, word2 = two_words.split()	#split into a list of words

		valid_input_bool = True
	except ValueError:
		print ("Bad input.")

if are_anagrams(word1, word2):	#return true or false
	print ("the words {} are anagrams.".format(word1, word2))
else:
	print ("the words {} are not anagrams.".format(word1, word2))
