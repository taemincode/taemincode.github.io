#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int points(string player);

int main(void)
{
    // Gets the words from the user
    string player1 = get_string("Player 1: ");
    string player2 = get_string("Player 2: ");

    // Finds out the points
    int point1 = points(player1);
    int point2 = points(player2);

    // Compares the points
    if (point2 > point2)
    {
        printf("Player 1 wins!\n");
    }
    else if (point1 < point2)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}

// Function to calculate points
int points(string player)
{
    int points = 0;
    for (int i = 0, l = strlen(player); i < l; i++)
    {
        player[i] = toupper(player[i]);
        if (player[i] == 'A' || player[i] == 'E' || player[i] == 'I' || player[i] == 'L' ||
            player[i] == 'N' || player[i] == 'O' || player[i] == 'R' || player[i] == 'S' ||
            player[i] == 'T' || player[i] == 'U')
        {
            points++;
        }
        else if (player[i] == 'D' || player[i] == 'G')
        {
            points += 2;
        }
        else if (player[i] == 'B' || player[i] == 'C' || player[i] == 'M' || player[i] == 'P')
        {
            points += 3;
        }
        else if (player[i] == 'F' || player[i] == 'H' || player[i] == 'V' || player[i] == 'W' ||
                 player[i] == 'Y')
        {
            points += 4;
        }
        else if (player[i] == 'K')
        {
            points += 5;
        }
        else if (player[i] == 'J' || player[i] == 'X')
        {
            points += 8;
        }
        else if (player[i] == 'Q' || player[i] == 'Z')
        {
            points += 10;
        }
    }

    return points;
}
