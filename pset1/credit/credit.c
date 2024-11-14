#include <cs50.h>
#include <stdio.h>

int get_starting_digits(long number, int digit_count, int n);
int main(void)
{
    long number;
    do
    {
        number = get_long("Number: ");
    }
    while (number < 0);

    int addition_of_digit_by_2 = 0;
    long number_2 = number;
    while (number_2 > 9)
    {
        int i = (number_2 % 100 - number_2 % 10) / 10 * 2;
        if (i >= 10)
        {
            i = (i - i % 10) / 10 + i % 10;
        }
        addition_of_digit_by_2 += i;
        number_2 = (number_2 - number_2 % 100) / 100;
    }

    int addition_final = addition_of_digit_by_2;
    long number_3 = number;
    while (number_3 > 0)
    {
        addition_final += number_3 % 10;
        number_3 = (number_3 - number_3 % 100) / 100;
    }

    int digit_count = 1;
    long number_4 = number;
    while (number_4 >= 10)
    {
        number_4 /= 10;
        digit_count++;
    }

    int starting_digit_1 = get_starting_digits(number, digit_count, 1);
    int starting_digit_2 = get_starting_digits(number, digit_count, 2);

    if (addition_final % 10 != 0)
    {
        printf("INVALID\n");
    }
    else if (digit_count == 13 && starting_digit_1 == 4)
    {
        printf("VISA\n");
    }
    else if (digit_count == 15 && (starting_digit_2 == 34 || starting_digit_2 == 37))
    {
        printf("AMEX\n");
    }
    else if (digit_count == 16 && (starting_digit_2 >= 51 && starting_digit_2 <= 55))
    {
        printf("MASTERCARD\n");
    }
    else if (digit_count == 16 && starting_digit_1 == 4)
    {
        printf("VISA\n");
    }
    else
    {
        printf("INVALID\n");
    }
}

int get_starting_digits(long number, int digit_count, int n)
{
    long tool = 1;
    for (int i = 0; i < digit_count - n; i++)
    {
        tool *= 10;
    }
    return number / tool;
}
