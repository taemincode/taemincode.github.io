#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int first_side = ("What is the length of the first side? \n");
    int second_side = ("What is the length of the second side? \n");
    int third_side = ("What is the length of the third side? \n");

    if (valid_triangle(first_side, second_side, thrid_side) == true)
    {
        printf("It's a valid triangle\n");
    }
    else
    {
        printf("It's an invalid triangle\n");
    }
}

bool valid_triangle()
