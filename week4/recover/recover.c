#include <stdio.h>
#include <stdlib.h>

typedef uint8_t BYTE

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }

    FILE *card = fopen(argv[1], "r");

    BYTE buff[512];

    while (fread(buff, 512, 1, card) == 512)
    {
        fread(buff, 512, 1, card);
        int file_count == 0;
        FILE *filename;

        if (buff[0] == 0xff && buff[1] == 0xd8 && buff[2] == 0xff && (buff[3] & 0xf0) == 0xe0)
        {
            if (file_count == 0)
            {
                sprintf(filename, "%03i.jpg", file_count)
            }
            else
            {
                fclose(filename)
                sprintf(filename, "%03i.jpg", file_count)
            }
            fwrite(buffer, 512, 1, filename)
        }
        else
        {

        }
    }
}
