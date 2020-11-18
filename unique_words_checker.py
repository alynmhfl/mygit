def make_word_list(a_file):
    word_list=[]
#create a list of words from text file
    for line_str in a_file:    #read line by line
        line_list=line_str.split()  #split each line into list of words
        for word in line_list:      #get words one line at a time from list
            if word !="--":         #if word is not '--'
                word_list.append(word)  #add word to speech list
    return word_list

def make_unique(word_list):    #create a list of unique words
    unique_list=[]             

    for word in word_list:
        if word not in unique_list:    #if word is not already in unique list
            unique_list.append(word)   #add to unique list
    return unique_list

gba_file=open('gettysburg.txt', 'r')
speech_list=make_word_list(gba_file)

print(speech_list)
print('speech length: ', len(speech_list))
print('unique length: ', len(make_unique(speech_list)))