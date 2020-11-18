def make_word_list(a_file):
  word_list = []
  
  for line_str in a_file:		
    line_list = line_str.split()	
    for word in line_list:
      if word != "--":		
        word_list.append(word)
  
  return word_list

def make_unique(word_list):
    unique_list=[]             

    for word in word_list:
        if word not in unique_list:
            unique_list.append(word)
    return unique_list

speech_file=open('speech.txt', 'r')
file_list=make_word_list(speech_file)

print(file_list)
print('speech length: ', len(file_list))
print('unique length: ', len(make_unique(file_list)))