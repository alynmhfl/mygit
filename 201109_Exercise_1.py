# Open file for writing
# Creates file if not exist
#Overwrites file if exist

temp_file = open("temp.txt", "w")
print("first line", file = temp_file)
print("second line", file = temp_file)
temp_file.close()