#include <stdio.h>

void meow(int n);

int main(void)
{
    for (int i = 0; i < 3; i++)
    {
        meow(3);
    }
}

void meow(int n)
{
    for (int i = 0; i < n; i++)
    {
        print("meow\n")
    }
}
