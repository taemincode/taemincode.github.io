#include <cs50.h>
#include <stdio.h>

int main(void)
{
    float sides[3];
    sides[0] = ("What is the length of the first side? \n");
    sides[1] = ("What is the length of the second side? \n");
    sides[2] = ("What is the length of the third side? \n");

    if (valid_triangle(first_side, second_side, thrid_side) == true)
    {
        printf("It's a valid triangle\n");
    }
    else
    {
        printf("It's an invalid triangle\n");
    }
}

bool valid_triangle(float a[])
{
    //Checks if all three sides are  positive
    if (a[0] < 0 || a[1] < 0 || a[2] < 0)
    {
        return false;
    }

    for (int i = 0; i < 3; i++)
    {
        
    }

}
