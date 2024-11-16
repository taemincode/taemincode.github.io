#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int change_owed;
    do
    {
        change_owed = get_int("Chage owed: ");
    }
    while (change_owed < 0);

    int number_of_coins_given = 0;
    while (change_owed > 0)
    {
        if (change_owed >= 25)
        {
            change_owed -= 25;
            number_of_coins_given++;
        }
        else if (change_owed >= 10)
        {
            change_owed -= 10;
            number_of_coins_given++;
        }
        else if (change_owed >= 5)
        {
            change_owed -= 5;
            number_of_coins_given++;
        }
        else if (change_owed >= 1)
        {
            change_owed--;
            number_of_coins_given++;
        }
    }

    printf("%i\n", number_of_coins_given);
}
