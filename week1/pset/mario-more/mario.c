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
        printf("\n");
    }
}

void brick_f(int number_of_bricks);
void row(int space, int brick)
{
    for (int i = 0; i < space; i++)
    {
        printf(" ");
    }
    brick_f(brick);
    printf("  ");
    brick_f(brick);
}

void brick_f(int number_of_bricks)
{
    for (int j = 0; j < number_of_bricks; j++)
    {
        printf("#");
    }
}
