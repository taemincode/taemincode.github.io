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
    if (side1 < 0 || side2 < 0 || side3 < 0)
    {
        return false;
    }

    //Finds out the largest side
    float largest_side = 0;
    for (int i = 0; i < 3; i++)
    {
        if (a[i] > largest_side)
        {
            largest_side = a[i];
        }
    }

    //Finds out if it's a valid triangle
    if (largest_side < )

}
