#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, string argv[])
{
    // Checks if the key is valid
    if (argc != 2)
    {
        printf("Useage: ./caesar key\n");
        return 1;
    }

    // Checks if the key is a digit
    for (int i = 0, l = strlen(argv[1]); i < l; i++)
    {
        if (isdigit(argv[1][i]) == false);
        printf("Useage: ./caesar key\n");
        return 2;
    }

    // Gets plaintext from the user
    string plaintext = get_string("plaintext:  ");

    // Defines key
    int key = atoi(argv[1]);

    // Computes Ciphertext
    int length = strlen(plaintext);
    string ciphertext[length]
    for (int i = 0, l = length; i < l; i++)
    {
        if (isalpha(plaintext[i]) == true)
        {
            if (isupper(plaintext[i]) == true)
            {
                plaintext[i]
            }
    }


}
