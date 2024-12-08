#include "helpers.h"
#include <stdio.h>
#include <math.h>

int sum_color(int height, int width, RGBTRIPLE image[height][width], int i, int j, char color);
int get_color_value(RGBTRIPLE pixel, char color);
int gx(int top_left, int top, int top_right, int left, int middle, int right, int bottom_right, int bottom, int bottom_left);

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

            image[i][j].rgbtRed = image[i][width - 1- j].rgbtRed;
            image[i][j].rgbtGreen = image[i][width - 1 - j].rgbtGreen;
            image[i][j].rgbtBlue = image[i][width - 1 - j].rgbtBlue;

            image[i][width - 1 - j].rgbtRed = tmp.rgbtRed;
            image[i][width - 1 - j].rgbtGreen = tmp.rgbtGreen;
            image[i][width - 1 - j].rgbtBlue = tmp.rgbtBlue;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE tmp[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            tmp[i][j].rgbtRed = sum_color(height, width, image, i, j, 'R');
            tmp[i][j].rgbtGreen = sum_color(height, width, image, i, j, 'G');
            tmp[i][j].rgbtBlue = sum_color(height, width, image, i, j, 'B');
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j].rgbtRed = tmp[i][j].rgbtRed;
            image[i][j].rgbtGreen = tmp[i][j].rgbtGreen;
            image[i][j].rgbtBlue = tmp[i][j].rgbtBlue;
        }
    }

    return;
}

int sum_color(int height, int width, RGBTRIPLE image[height][width], int i, int j, char color)
{
    int sum = 0;
    int num = 0;

    if (i == 0)
    {
        if (j == 0)
        {
            sum += get_color_value(image[i][j], color) +
                   get_color_value(image[i][j + 1], color) +
                   get_color_value(image[i + 1][j], color) +
                   get_color_value(image[i + 1][j + 1], color);
            num = 4;
        }
        else if (j == width - 1)
        {
            sum += get_color_value(image[i][j], color) +
                   get_color_value(image[i][j - 1], color) +
                   get_color_value(image[i + 1][j - 1], color) +
                   get_color_value(image[i + 1][j], color);
            num = 4;
        }
        else
        {
            sum += get_color_value(image[i][j], color) +
                   get_color_value(image[i][j - 1], color) +
                   get_color_value(image[i][j + 1], color) +
                   get_color_value(image[i + 1][j - 1], color) +
                   get_color_value(image[i + 1][j], color) +
                   get_color_value(image[i + 1][j + 1], color);
            num = 6;
        }
    }
    else if (i == height - 1)
    {
        if (j == 0)
        {
            sum += get_color_value(image[i][j], color) +
                   get_color_value(image[i][j + 1], color) +
                   get_color_value(image[i - 1][j], color) +
                   get_color_value(image[i - 1][j + 1], color);
            num = 4;
        }
        else if (j == width - 1)
        {
            sum += get_color_value(image[i][j], color) +
                   get_color_value(image[i][j - 1], color) +
                   get_color_value(image[i - 1][j - 1], color) +
                   get_color_value(image[i - 1][j], color);
            num = 4;
        }
        else
        {
            sum += get_color_value(image[i][j], color) +
                   get_color_value(image[i][j - 1], color) +
                   get_color_value(image[i][j + 1], color) +
                   get_color_value(image[i - 1][j - 1], color) +
                   get_color_value(image[i - 1][j], color) +
                   get_color_value(image[i - 1][j + 1], color);
            num = 6;
        }
    }
    else
    {
        if (j == 0)
        {
            sum += get_color_value(image[i + 1][j], color) +
                   get_color_value(image[i + 1][j + 1], color) +
                   get_color_value(image[i][j], color) +
                   get_color_value(image[i][j + 1], color) +
                   get_color_value(image[i - 1][j], color) +
                   get_color_value(image[i - 1][j + 1], color);
            num = 6;
        }
        else if (j == width - 1)
        {
            sum += get_color_value(image[i + 1][j - 1], color) +
                   get_color_value(image[i + 1][j], color) +
                   get_color_value(image[i][j - 1], color) +
                   get_color_value(image[i][j], color) +
                   get_color_value(image[i - 1][j - 1], color) +
                   get_color_value(image[i - 1][j], color);
            num = 6;
        }
        else
        {
            sum += get_color_value(image[i + 1][j - 1], color) +
                   get_color_value(image[i + 1][j], color) +
                   get_color_value(image[i + 1][j + 1], color) +
                   get_color_value(image[i][j - 1], color) +
                   get_color_value(image[i][j], color) +
                   get_color_value(image[i][j + 1], color) +
                   get_color_value(image[i - 1][j - 1], color) +
                   get_color_value(image[i - 1][j], color) +
                   get_color_value(image[i - 1][j + 1], color);
            num = 9;
        }
    }

    return round((double)sum / (double)num);
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
    RGBTRIPLE tmp[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            tmp[i][j].rgbtRed = edge(height, width, image, i, j, 'R');
            tmp[i][j].rgbtGreen = edge(height, width, image, i, j, 'G');
            tmp[i][j].rgbtBlue = edge(height, width, image, i, j, 'B');
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j].rgbtRed = tmp[i][j].rgbtRed;
            image[i][j].rgbtGreen = tmp[i][j].rgbtGreen;
            image[i][j].rgbtBlue = tmp[i][j].rgbtBlue;
        }
    }

    return;
}

int sum_color(int height, int width, RGBTRIPLE image[height][width], int i, int j, char color)
{
    int gx = 0;
    int gy = 0;

    if (i == 0)
    {
        if (j == 0)
        {
            gx = gx(get_color_value(image[i - 1][j - 1], color), get_color_value(image[i - 1][j], color), get_color_value(image[i - 1][j + 1], color),
                    get_color_value(image[i][j - 1], color), get_color_value(image[i][j], color), get_color_value(image[i][j + 1], color),
                    get_color_value(image[i + 1][j - 1], color), get_color_value(image[i + 1][j], color), get_color_value(image[i + 1][j + 1], color))
        }
        else if (j == width - 1)
        {
            sum += get_color_value(image[i][j], color) +
                   get_color_value(image[i][j - 1], color) +
                   get_color_value(image[i + 1][j - 1], color) +
                   get_color_value(image[i + 1][j], color);
        }
        else
        {
            sum += get_color_value(image[i][j], color) +
                   get_color_value(image[i][j - 1], color) +
                   get_color_value(image[i][j + 1], color) +
                   get_color_value(image[i + 1][j - 1], color) +
                   get_color_value(image[i + 1][j], color) +
                   get_color_value(image[i + 1][j + 1], color);
        }
    }
    else if (i == height - 1)
    {
        if (j == 0)
        {
            sum += get_color_value(image[i][j], color) +
                   get_color_value(image[i][j + 1], color) +
                   get_color_value(image[i - 1][j], color) +
                   get_color_value(image[i - 1][j + 1], color);
        }
        else if (j == width - 1)
        {
            sum += get_color_value(image[i][j], color) +
                   get_color_value(image[i][j - 1], color) +
                   get_color_value(image[i - 1][j - 1], color) +
                   get_color_value(image[i - 1][j], color);
        }
        else
        {
            sum += get_color_value(image[i][j], color) +
                   get_color_value(image[i][j - 1], color) +
                   get_color_value(image[i][j + 1], color) +
                   get_color_value(image[i - 1][j - 1], color) +
                   get_color_value(image[i - 1][j], color) +
                   get_color_value(image[i - 1][j + 1], color);
        }
    }
    else
    {
        if (j == 0)
        {
            sum += get_color_value(image[i + 1][j], color) +
                   get_color_value(image[i + 1][j + 1], color) +
                   get_color_value(image[i][j], color) +
                   get_color_value(image[i][j + 1], color) +
                   get_color_value(image[i - 1][j], color) +
                   get_color_value(image[i - 1][j + 1], color);
        }
        else if (j == width - 1)
        {
            sum += get_color_value(image[i + 1][j - 1], color) +
                   get_color_value(image[i + 1][j], color) +
                   get_color_value(image[i][j - 1], color) +
                   get_color_value(image[i][j], color) +
                   get_color_value(image[i - 1][j - 1], color) +
                   get_color_value(image[i - 1][j], color);
        }
        else
        {
            sum += get_color_value(image[i + 1][j - 1], color) +
                   get_color_value(image[i + 1][j], color) +
                   get_color_value(image[i + 1][j + 1], color) +
                   get_color_value(image[i][j - 1], color) +
                   get_color_value(image[i][j], color) +
                   get_color_value(image[i][j + 1], color) +
                   get_color_value(image[i - 1][j - 1], color) +
                   get_color_value(image[i - 1][j], color) +
                   get_color_value(image[i - 1][j + 1], color);
        }
    }

    return round((double)sum / (double)num);
}

int gx(int top_left, int top, int top_right,
        int left, int middle, int right, int bottom_right,
        int bottom, int bottom_left)
{
    int gx = top_left * (-1) + top * 0 + top_right * (1) left * (-2) + middle * 0 + right * 2 + bottom_right * (-1) + bottom * 0 + bottom_left * 1;

    if (gx > 255)
    {
        gx = 255;
    }

    return gx;
}
