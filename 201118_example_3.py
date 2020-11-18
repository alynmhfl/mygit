# Create a list of words from the file

def make_word_list(a_file):
  
  word_list = []			# List of speech words: initialized to be empty
  
  for line_str in a_file:		# Read file line by line
    line_list = line_str.split()	# Split each line into a list of words
    for word in line_list:		# Get words one at a time from list
      if word != "--"			# If the word is not "--"
        word_list.append(word)		# Add the word to the speech list
  
  return word_list
