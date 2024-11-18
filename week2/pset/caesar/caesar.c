#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

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
        if (isdigit(argv[1][i]) == false)
        printf("Useage: ./caesar key\n");
        return 2;
    }

    // Gets plaintext from the user
    string plaintext = get_string("plaintext:  ");

    // Defines key
    int key = atoi(argv[1]);

    // Computes Ciphertext
    int length = strlen(plaintext);
    string ciphertext[length];
    for (int i = 0, l = length; i < l; i++)
    {
        // If plaintext[i] is alphabetical
        if (isalpha(plaintext[i]) == true)
        {
            char index_plain;
            char index_cipher;
            
            if (isupper(plaintext[i]) == true)
            {
                index_plain = plaintext[i] - 'A';
                index_cipher = (index_plain + key) % 26;
                ciphertext[i] = index_cipher + 'A';
            }
            else
            {
                index_plain = plaintext[i] - 'a';
                index_cipher = (index_plain + key) % 26;
                ciphertext[i] = index_cipher + 'a';
            }
        }
        // Else plaintext[i] is not alphabetical
        else
        {
            ciphertext[i] = plaintext[i];
        }
    }

    // Prints ciphertext
    printf("ciphertext: %s\n", ciphertext);
}
