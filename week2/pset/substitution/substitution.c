#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const int alphabet_length = 26;

void valid(int length, string key);

string cipher(string key, string text);

int main(int argc, string argv[])
{
    // Checks if the input is valid
    valid(argc, argv[1]);

    // Gets plaintext
    string plaintext = get_string("plaintext:  ");

    // Computes ciphertext
    string ciphertext = cipher(argv[1], plaintext);

    // Prints ciphertext
    printf("ciphertext: %s\n", ciphertext);

    // Free the allocated memory
    free(ciphertext);
}

void valid(int length, string key)
{
    // If the format is invalid
    if (length != 2)
    {
        printf("Usage: ./substitution key\n");
        exit(1);
    }

    // If the lenghth of the key is invalid
    if (strlen(key) != alphabet_length)
    {
        printf("Key must contain 26 characters.\n");
        exit(1);
    }

    // If the key is not alphabetic
    for (int i = 0; i < alphabet_length; i++)
    {
        if (!isalpha(key[i]))
        {
            printf("Usage: ./substitution key\n");
            exit(1);
        }
    }

    // If the key has same alphabets
    char upper_key[alphabet_length];
    for (int i = 0; i < alphabet_length; i++)
    {
        upper_key[i] = toupper(key[i]);
    }
    for (int i = 0; i < alphabet_length; i++)
    {
        int counter = 0;
        for (int j = 0; j < alphabet_length; j++)
        {
            if (key[i] == key[j])
            {
                counter++;
            }
        }
        if (counter != 1)
        {
            printf("Usage: ./substitution key\n");
            exit(1);
        }
    }
}

string cipher(string key, string text)
{
    char upper_key[alphabet_length];
    for (int i = 0; i < alphabet_length; i++)
    {
        upper_key[i] = toupper(key[i]);
    }
    int l = strlen(text);
    char *cipher = malloc(l + 1);
    if (cipher == NULL)
    {
        exit(1);
    }
    for (int i = 0; i < l; i++)
    {
        // If the 'i'th character of the plaintext is an alphbet
        if (isalpha(text[i]))
        {
            // If the character is uppercase
            if (isupper(text[i]))
            {
                cipher[i] = upper_key[text[i] - 'A'];
            }
            // Else the character is lowercase
            else
            {
                cipher[i] = tolower(upper_key[text[i] - 'a']);
            }
        }
        // Else the character is not an alphabet
        else
        {
            cipher[i] = text[i];
        }
    }
    // Null terminating
    cipher[l] = '\0';

    // Returns ciphertext
    return cipher;
}
