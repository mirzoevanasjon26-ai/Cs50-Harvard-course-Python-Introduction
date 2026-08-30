def double(n):
    return n * 2 


def tripple(n):
    return n * 3 

number = int(input("What's the number? "))

print("Original:", number)

number = double(number)
print("x2:", number)

number = tripple(number)
print("x3:", number)
