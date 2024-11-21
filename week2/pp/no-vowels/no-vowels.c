// Write a function to replace vowels with numbers
// Get practice with strings
// Get practice with command line
// Get practice with switch

#include <cs50.h>
#include <stdio.h>
#include <string.h>

string replace(string word);

int main(int argc, string argv[])
{
    //If the program is executed without any command-line
    //arguments or with more than one command-line argument
    if (argc != 2)
    {
        printf("Usage: ./no-vowels word\n");
        return 1;
    }

    // Prints out the replaced word
    printf("%s\n", replace(argv[1]));

}

string replace(string word)
{
    for (int i = 0, l = strlen(word); i < l; i++)
    {
        switch (word[i])
        {
            case 'A' || 'a':
                word[i] = '6';
                break;

            case 'E' || 'e':
                word[i] = '3';
                break;

            case 'I' || 'i':
                word[i] = '1';
                break;

            case 'O' || 'o':
                word[i] = '0'
                break;
        }
    }
    return word;
}
