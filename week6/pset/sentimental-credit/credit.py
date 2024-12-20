from cs50 import get_int


def main():
    while True:
        number = get_int("Number: ")
        if number > 0:
            break

    print(luhn(number))


def luhn(number):
    # If Amex
    if digit == 15:
        if


def digit(number)
    return len(str(number))


def square(base, exponent):
    if exponent == 1:
        return base
    else:
        return square(base, exponent - 1) * base


def starting(number, digit):
    return number - number % square(10, digit)
