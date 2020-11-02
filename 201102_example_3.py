# simple while

x_int = 0  # Initialize loop-control variable

# Test loop-control variable at the beginning of loop
while x_int < 10:
    print(x_int, end=' ')  # print the value of x_int each time through the while loop
    x_int = x_int + 1  # Change loop-control variable
    print()

print("Final value of x_int: ", x_int)
