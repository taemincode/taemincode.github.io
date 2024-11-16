#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string first_name = get_string("What is your frist name? ");
    string last_name = get_string("What is your last name? ");
    printf("Hello, %s %s\n", first_name, last_name);
}
