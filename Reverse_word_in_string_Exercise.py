#  Reverse word in string

my_str = 'This is a test'
string_element = my_str.split()
print(string_element)
reversed_element = []
for element in string_element:
    reversed_element.append(element[::-1])
print(reversed_element)