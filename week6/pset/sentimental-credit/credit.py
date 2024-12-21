from cs50 import get_int
from math import floor


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
    while tmp_2 > 0:
        sum += tmp_2 % 10
        tmp_2 = (tmp_2 - tmp_2 % 100) / 100

    # If the total’s last digit is 0 (or, put more formally, if the total modulo 10 is congruent to 0), the number is valid
    if sum % 10 == 0:
        return True
    else:
        return False


def card(number):
    card_length = digit(number)
    
    # If Amex
    if card_length == 15 and starting(number, 2, card_length) in {34, 37}:
        return "AMEX"
    # If Mastercard
    elif card_length == 16 and 51 <= starting(number, 2, card_length) <= 55:
        return "MASTERCARD"
    # If Visa
    elif card_length in {13, 16} and starting(number, 1, card_length) == 4:
        return "VISA"
    # Invalid
    return "Invalid"


def digit(number):
    return len(str(number))


def starting(number, len, digit):
    return floor(number / pow(10, digit - len))


main()
