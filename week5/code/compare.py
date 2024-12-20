from cs50 import get_int

x = get_int("What's x? ")
y = get_int("What's y? ")

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("X is equal to y")
