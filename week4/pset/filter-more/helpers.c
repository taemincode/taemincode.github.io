#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int avg_value = round((image[i][j].rgbtRed + image[i][j].rgbtGreen
             + image[i][j].rgbtBlue) / 3.0);
            image[i][j].rgbtRed = avg_value;
            image[i][j].rgbtGreen = avg_value;
            image[i][j].rgbtBlue = avg_value;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    int half;
    if (width % 2 == 0)
        half = width / 2;
    else
        half = width / 2 + 1;

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < half; j++)
        {
            RGBTRIPLE tmp;
            tmp.rgbtRed = image[i][j].rgbtRed;
            tmp.rgbtGreen = image[i][j].rgbtGreen;
            tmp.rgbtBlue = image[i][j].rgbtBlue;

            image[i][j].rgbtRed = image[i][width - j].rgbtRed;
            image[i][j].rgbtGreen = image[i][width - j].rgbtGreen;
            image[i][j].rgbtBlue = image[i][width - j].rgbtBlue;

            image[i][width - j].rgbtRed = tmp.rgbtRed;
            image[i][width - j].rgbtGreen = tmp.rgbtGreen;
            image[i][width - j].rgbtBlue = tmp.rgbtBlue;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    for (int = i; i < height; i++)
    {
        for (int = j; j < width; j++)
        {
            RGBTRIPLE avg_value;

            avg_value.rgbtRed += image[i][j].rgbtRed;
            if (i != 1)
            {
                if (j != 1)
                {
                    avg_value.rgbtRed += image[i - 1][j].rgbtRed
                     + imgae[i][j - 1].rgbtRed + imgae[i - 1][j - 1].rgbtRed;
                }
                else
                {
                    avg_value.rgbtRed += image[i - 1][j].rgbtRed +
                }
            }
        }
    }

    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
