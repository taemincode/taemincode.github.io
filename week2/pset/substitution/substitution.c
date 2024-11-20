#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdilib.h>
#include <string.h>


void valid(int length, string key);

string cipher(string key, string text);

int main(int argc, string argv[])
{
    // Checks if the input is valid
    valid(argc, argv[1]);

    // Gets plaintext
    string plain = get_string("plaintext:  ");

    // Computes ciphertext
    string cipher = cipher(argv[1], plain)
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
    if (isalpha(key) == false)
    {
        exit(1);
    }

    // If the key has same alphabets
    string upper_key = toupper(key);
    for (int i = 0; i < 26; i++)
    {
        int counter = 0;
        for (int j = 0; j < l; j++)
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
    for (int i = 0, j = 65; i < 26; i++)
    {

    }
}
