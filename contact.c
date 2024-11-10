#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string name = get_string("What is the person's name? ");
    int age = get_int("What is %s's age? ", name);
    int phone_number = get_int("What is %s's phone number? ", name);
    printf("Name: %s\nAge: %i\nPhone number: %i\n", name, age, phone_number);
}
