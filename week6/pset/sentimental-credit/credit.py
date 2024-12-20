from cs50 import get_int


def main():
    while True:
        number = get_int("Number: ")
        if number > 0:
            break

    if luhn(number):
        print(card(number))
    else:
        print("Invalid")


def luhn(number):
    # Multiply every other digit by 2, starting with the number’s second-to-last digit, and then add those products’ digits together
    sum = 0
    tmp = number
    while tmp >= 10:
        i = (tmp % 100 - tmp % 10) / 10 * 2
        if i >= 10:
            i = (i - i % 10) / 10 + i % 10
        sum += i
        tmp = (tmp - tmp % 100) / 100

    # Add the sum to the sum of the digits that weren’t multiplied by 2
    tmp_2 = number
    while tmp_2 >= 10:
        sum += tmp_2 % 10
        tmp_2 = (tmp_2 - tmp_2 % 100) / 100

    # If the total’s last digit is 0 (or, put more formally, if the total modulo 10 is congruent to 0), the number is valid
    if sum % 10 == 0:
        return True
    else:
        return False


def card(number):
    # If Amex
    if digit(number) == 15:
        if starting(number, 2, digit(number)) == 34 or starting(number, 2, digit(number)) == 37:
            return "AMEX"
    # If Mastercard
    elif digit(number) == 16:
        if starting(number, 2, digit(number)) >= 51 and starting(number, 2, digit(number)) <= 55:
            return "MASTERCARD"
    # If Visa
    elif digit(number) == 13 or digit(number) == 16:
        if starting(number, 1, digit(number)) == 4:
            return "VISA"
    # Invalid
    else:
        return "Invalid"


def digit(number):
    return len(str(number))


def square(base, exponent):
    if exponent == 1:
        return base
    else:
        return square(base, exponent - 1) * base


def starting(number, len, digit):
    return (number - number % square(10, digit - len)) / square(10, digit - len)


main()
