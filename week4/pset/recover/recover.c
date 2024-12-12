#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }

    FILE *card = fopen(argv[1], "r");
    if (card == NULL)
    {
        return 2;
    }

    BYTE buff[512];

    int file_count = 0;
    char filename[8];
    FILE *img = NULL;

    fread(buff, 512, 1, card);

    while (fread(buff, 512, 1, card) == 512)
    {
        if (buff[0] == 0xff && buff[1] == 0xd8 && buff[2] == 0xff && (buff[3] & 0xf0) == 0xe0)
        {
            if (file_count > 0)
            {
                fclose(img);
            }
            sprintf(filename, "%03i.jpg", file_count);

            img = fopen(filename, "a");
            if (img == NULL)
            {
                return 1;
            }

            fwrite(buff, 512, 1, img);

            file_count++;
        }
        else if (file_count > 0)
        {
            fwrite(buff, 512, 1, img);
        }
        fread(buff, 512, 1, card);
    }
    if (img != NULL)
    {
        fclose(img);
    }
    fclose(card);
}
