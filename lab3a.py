# Nirel Marie M. Ibarra
# 192468
# March 15, 2021

# I have not discussed the Python language code in my program
# with anyone other than my instructor or the teaching assistants
# assigned to this course

# I have not used Python language code obatained from another student
# or any other unauthorized source, either modified or unmodified

# If any Python language code or documentation used in my program 
# was obtained from another source, such as a textbook or website,
# that has clearly noted with a proper ciration in the comments
# of my program

#closest answer
#infinitely asks prompt unless number is outside the range

total = 0
maximum = None
minimum = None

number = int(input())
while total < number:
    new_num = int(input())
    if maximum is None or maximum < new_num:
        maximum = new_num
    elif minimum is None or minimum > new_num:
        minimum = new_num
    total += 1

diff = maximum - minimum

print("Maximum =", maximum)
print("Minimum =", minimum)
print("Range =", str(diff))

