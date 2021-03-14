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

def difference(a, b):
    if a > b:
        difference = a - b
    elif a < b:
        difference = b - a
    return difference

cases = int(input())
total = 0
while total < cases:
    case_a = int(input())
    case_b = int(input())
    print(difference(case_a, case_b))
    total += 1
    