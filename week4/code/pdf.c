#include <cs50.h>
#include <stdio.h>

typedef unit_8 

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./pdf file_name")
        return 1;
    }

    FILE *f = fopen(argv[1], "r")

    char *buffer = malloc(4 * sizeof(char));

    fread(buffer, 1BYTE)
}
