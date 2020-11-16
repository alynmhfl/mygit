# Open file named "dictionary.txt" for reading ('r')
data_file = open("dictionary.txt", 'r')

# Return word in lowercase stripped of whitespace
def clean_word(word):
  return word.strip().lower()

# Reutrn vowels in string word -- include repeats.
def get_vowels_in_word(word):
  vowel_str = "aeiou"
  vowels_in_word = ""
  for char in word:
    if char in vowel_str:
      vowels_in_word += char
  return vowels_in_word

# Main program
print("Find words containing vowels 'aeiou' in that order:")
for word in data_file:				# for each word in the file
  word = clean_word(word)			# clean the word
  if len(word) <= 6:				# if word is too small, skip it
    continue
  vowel_str = get_vowels_in_word(word)		# get vowels in word
  if vowel_str == 'aeiou':			# check if you have exactly all vowels in order
    print(word)
