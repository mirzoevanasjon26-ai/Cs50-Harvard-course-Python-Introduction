#split() --> to devide a string into smaller parts.


name = input("What's your name? ").strip().capitalize()
first, last = name.split()

print(f"Hello, {first}")
