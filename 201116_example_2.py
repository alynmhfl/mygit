#Print all words in a dictionary file that has one word per line

#Open file named "dictionary.txt" for reading('r)
data_file = open("dictionary.txt", 'r')

#Iterate through the file one line at a time
for line_str in data_file:
  print(line_str)
