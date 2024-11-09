#include <stdio.h>
#include <cs50.h>

int add(void);

int main(void)
{
    int x = get_int("x: ");
    int y = get_int("y: ");

    int z = add();
    printf("%i\n", z);
}

int add(int x, int y)
{
    return x + y;
}
