data_file = open("dictionary.txt", 'r')

def clean_word(word):
  """Return word in lowercase stripped of whitespace."""
  return word.strip().lower()

def get_vowels_in_word(word):
  """Return Vowels in string word - include repeats."""
  vowel_str = "aeiou"
  vowels_in_word = " "
  for char in word:
    if char in vowel_str:
      vowels_in_word += char
  return vowels_in_word

#Main program
print("Find words containing vowels 'aeiou' in that order:")
for word in data_file:
  word = clean_word(word)
  if len(word)<=6:
    continue
  vowel_str = get_vowels_in_word(word)
  if vowel_str == 'aeiou' :
    print(word)
