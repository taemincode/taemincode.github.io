#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int sequence[5];

    for (int i = 0; i < 5; i++)
    {
        sequence[i] = sequence[i - 1] * 2;
        printf("%i\n", sequence[i]);
    }
}
