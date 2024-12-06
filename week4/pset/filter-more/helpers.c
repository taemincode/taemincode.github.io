#include "helpers.h"
#include <math.h>

int sum_color(int height, int width, RGBTRIPLE image[height][width], int i, int j, char color);
int get_color_value(RGBTRIPLE pixel, char color);

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
            image[height][width].rgbtRed = sum_color(height, width, image[height][width].rgbtRed, i, j, R);
            image[height][width].rgbtGreen = sum_color(height, width, image[height][width].rgbtGreen, i, j);
            image[height][width].rgbtBlue = sum_color(height, width, image[height][width].rgbtBlue, i, j);
        }
    }

    return;
}

int sum_color(int height, int width, int value_for_color, int i, int j)
{
    int sum = 0;
    int num = 0;

    if (i == 1)
        {
            if (j == 1)
            {
                sum += image[i][j].rgbtRed + image[i][j + 1].rgbtRed + image[i - 1][j].rgbtRed + image[i - 1][j + 1].rgbtRed;
                num = 4;
            }
            else if (j == width - 1)
            {
                sum += image[i][j].rgbtRed + image[i][j - 1].rgbtRed + image[i - 1][j - 1].rgbtRed + image[i - 1][j].rgbtRed;
                num = 4;
            }
            else
            {
                sum += image[i][j].rgbtRed + image[i][j - 1].rgbtRed + image[i][j + 1].rgbtRed + image[i - 1][j - 1].rgbtRed + image[i - 1][j].rgbtRed + image[i - 1][j + 1].rgbtRed;
                num = 6;
            }
        }
        else if (i == height - 1)
        {
            if (j == 1)
            {
                sum += image[i][j].rgbtRed + image[i][j + 1].rgbtRed + image[i + 1][j].rgbtRed + image[i + 1][j + 1].rgbtRed;
                num = 4;
            }
            else if (j == width - 1)
            {
                sum += image[i][j].rgbtRed + image[i][j - 1].rgbtRed + image[i + 1][j - 1].rgbtRed + image[i + 1][j].rgbtRed;
                num = 4;
            }
            else
            {
                sum += image[i][j].rgbtRed + image[i][j - 1].rgbtRed + image[i][j + 1].rgbtRed + image[i + 1][j - 1].rgbtRed + image[i + 1][j].rgbtRed + image[i +1][j + 1].rgbtRed;
                num = 6;
            }
        }
        else
        {
            if (j == 1)
            {
                sum += image[i + 1][j].rgbtRed + image[i + 1][j + 1].rgbtRed + image[i][j].rgbtRed + image[i][j + 1].rgbtRed + image[i - 1][j].rgbtRed + image[i - 1][j + 1].rgbtRed;
                num = 6;
            }
            else if (j == width - 1)
            {
                sum += image[i + 1][j - 1].rgbtRed + image[i + 1][j].rgbtRed + image[i][j - 1].rgbtRed + image[i][j].rgbtRed + image[i - 1][j - 1].rgbtRed + image[i - 1][j].rgbtRed;
                num = 6;
            }
            else
            {
                sum += image[i + 1][j - 1].rgbtRed + image[i + 1][j].rgbtRed + image[i + 1][j + 1].rgbtRed + image[i][j - 1].rgbtRed + image[i][j].rgbtRed + image[i][j + 1].rgbtRed + image[i - 1][j - 1].rgbtRed + image[i - 1][j].rgbtRed + image[i - 1][j + 1].rgbtRed;
                num = 9;
            }
    }

    return sum / num;
}

int get_color_value(RGBTRIPLE pixel, char color)
{
    if (color == 'R')
        return pixel.rgbtRed;
    else if (color == 'G')
        return pixel.rgbtGreen;
    else
        return pixel.rgbtBlue;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
