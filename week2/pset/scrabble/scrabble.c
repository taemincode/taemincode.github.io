#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string player1 = get_string("Player 1: ");
    string player2 = get_string("Player 2: ");

}

int points(string player)
{
    int points = 0;
    player = toupper(player);
    for(int i = 0, l = strlen(player); i < l; i++)
    {
        if ('A' <= player[i] <= 'Z')
        {
            
        }
    }
}
