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

def negate(a):
    neg = -a
    return neg

def add(a, b):
    total = a + b
    return total

def maximum(a, b, c):
    if a > b and a > c:
        big = a
    elif b > a and b > c:
        big = b
    elif c > a and c > b:
        big = c
    return big

while True:
    prompt = input()
    if prompt == "negate":
        number = int(input())
        print(negate(number))
        continue
        
    elif prompt == "add":
        number_a = int(input())
        number_b = int(input())
        print(add(number_a, number_b))
        continue
        
    elif prompt == "maximum":
        number_a = int(input())
        number_b = int(input())
        number_c = int(input())
        print(maximum(number_a, number_b, number_c))
        continue
    elif prompt == "stop":
        break
        
