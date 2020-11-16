#print all the words in a dictionar file
# that has one word per line

#open file named "dictionary.txt" for reading('r')
data_file = open("dictionary.txt",'r')
#itirate through the file one line at a time
for line_str in data_file:
    print(line_str)