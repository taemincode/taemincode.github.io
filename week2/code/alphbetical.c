#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string phrase = get_string("Enter a phrase: ");
    int length = strlen(phrase);
    for (int i = 0; i < length; i++)
    {
        printf("%c", phrase[i]);
    }
    printf("\n");
}
