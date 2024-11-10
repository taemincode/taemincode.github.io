#include <cs50.h>
#include <stdio.h>

void print_row(int legnth);
int main(void)
{
    int height = get_int("Height: ");
    int i = 0;
    while(i < height)
    {
        print_row(i + 1);
        i++;
    }
}

void print_row(int length)
{
    for (int i = 0; i < length; i++)
    {
        printf("#");
    }
    printf("\n");
}
