#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


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
}

void valid(int length, string key)
{
    // If the format is invalid
    if (length != 2)
    {
        exit(1);
    }

    // If the lenghth of the key is invalid
    if (strlen(key) != 26)
    {
        exit(1);
    }

    // If the key is not alphabetic
    for (int i = 0; i < 26; i++)
    {
        if (!isalpha(key[i]))
        {
            exit(1);
        }
    }

    // If the key has same alphabets
    char upper_key[26];
    for (int i = 0; i < 26; i++)
    {
        upper_key[i] = toupper(key[i]);
    }
    for (int i = 0; i < 26; i++)
    {
        int counter = 0;
        for (int j = 0; j < 26; j++)
        {
            if (key[i] == key[j])
            {
                counter++;
            }
        }
        if (counter != 1)
        {
            exit(1);
        }
    }

}

string cipher(string key, string text)
{
    upper_key = toupper(key);
    l = strlen(text);
    char cipher[l + 1];
    for (int i = 0; i < l; i++)
    {
        // If the 'i'th character of the plaintext is an alphbet
        if (isalhpa(text[i]))
        {
            // If the character is uppercase
            if (isupper(text[i]))
            {
                cipher[i] = upper_key[text[i] - 65];
            }
            // Else the character is lowercase
            else
            {
                cipher[i] = tolower(upper_key[text[i] - 65]);
            }
        }
        // Else the character is not an alphabet
        else
        {
            cipher[i] = text[i];
        }
    }
    // Null terminating
    cipher[l] = \0;

    // Returns ciphertext
    return cipher;
}
