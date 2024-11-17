#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int sequence[5];

    for (int i = 0,  n = 1; i < 5; i++)
    {
        sequence[i] = n;
        printf("%i\n", sequence[i]);
        n *= 2;
    }
}
