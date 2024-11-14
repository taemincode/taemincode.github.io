#include <cs50.h>
#include <stdio.h>

int main(void)
{
    float input = get_float("Number: ");
    float number = 5.0;
    int output = number / input % 1.0;
    printf("%i\n", output);
}
