# Gettysburg Address analysis
# Count words, unique words

def make_word_list(a_file):
    word_list = []
    for line_str in a_file:
        line_list = line_str.split()
        for word in line_list:
            if word != '--':
                word_list.append(word)
    return word_list


def make_unique(word_list):
    """Create a list of unique words"""
    unique_list = []

    for word in word_list:
        if word not in unique_list:
            unique_list.append(word)
    return unique_list


# Main code
gba_file = open("gettysburg.txt", "r")
speech_list = make_word_list(gba_file)

#  Print the speech and length
print(speech_list)
print("Speech Length:", len(speech_list))
print("Unique Word", len(make_unique(speech_list)))
