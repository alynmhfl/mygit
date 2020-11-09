# read a particular line from a file. User provides both line
# number and the file name

file_str = input("Open what file: ")
find_line_str = input("which line(integer): ")

try:
    input_file = open(file_str) # Potential user error
    find_line_int = int(find_line_str) # Potential user error
    line_count_int = 1
    for line_str in input_file:
        if line_count_int == find_line_int:
            print("Line {} of file {} is {}".format(find_line_int,file_str, line_str))
            break
        line_count_int += 1
    else:
        # get here if line sought doesnt exist
        print("Line {} if file {} not found".format(find_line_int, find_line_str))
    input_file.close()
except IOError:
    while True:
        file_str = input("That file was not found. Please try again:")
except ValueError:
    find_line_str = input("Invalid line value. Please try again:")

print("End of the program")