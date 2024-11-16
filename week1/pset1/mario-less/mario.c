#include <cs50.h>
#include <stdio.h>

void row(int space, int brick);
int main(void)
{
    int height;
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1);

    for (int i = 0; i < height; i++)
    {
        row(height - (i + 1), i + 1);
    }
}

void row(int space, int brick)
{
    for (int i = 0; i < space; i++)
    {
        printf(" ");
    }
    for (int j = 0; j < brick; j++)
    {
        printf("#");
    }
    printf("\n");
}
