count = 1
total = 0

# BUG: Added the missing colon (:) at the end of the while condition.
# Without the colon, Python gives a syntax error.
while count <= 5:
    total = total + count

    # BUG: The original condition was count < 5, which stopped at 4.
    # Using <= 5 makes the loop include the number 5.
    count = count + 1

# BUG: Converted total to a string so it can be joined with the text.
# The original code tried to add a string and an integer together.
print("Sum of 1 to 5 is: " + str(total))