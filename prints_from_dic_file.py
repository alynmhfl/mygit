#prints all words in text file that has one word per line
datafile=open('dictionary.txt','r')
for line_str in datafile:
    print(line_str)
