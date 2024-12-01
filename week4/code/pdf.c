#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./pdf file_name\n");
        return 1;
    }

    FILE *f = fopen(argv[1], "r");

    char *buffer = malloc(4 * sizeof(char));

    fread(buffer, 1, 4, argv[1]);
    if (buffer[0] == 37, buffer[1] == 80, buffer[2] == 68, buffer[3] == 70)
    {
        printf("Is a PDF file\n");
        return 0;
    }
    else
    {
        printf("Is not a PDF file\n");
        return 0;
    }

    free(buffer);
}
