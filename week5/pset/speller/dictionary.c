// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// Counter for the size function
unsigned int COUNT = 0;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N][N][N];

// Hashes word to a number
unsigned int first_hash(const char *word)
{
    return toupper(word[0]) - 'A';
}

unsigned int second_hash(const char *word)
{
    return toupper(word[1]) - 'A';
}

unsigned int third_hash(const char *word)
{
    return toupper(word[2]) - 'A';
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            for (int k = 0; k < N; k++)
            {
                table[i][j][k] = NULL;
            }
        }
    }

    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        return false;
    }

    char word[LENGTH + 1];

    while (fscanf(file, "%s", word) != EOF)
    {
        node *new_node = malloc(sizeof(node));
        if (new_node == NULL)
        {
            return false;
        }

        strcpy(new_node->word, word);
        new_node->next = NULL;

        new_node->next = table[first_hash(word)][second_hash(word)][third_hash(word)];
        table[first_hash(word)][second_hash(word)][third_hash(word)] = new_node;

        COUNT++;
    }
    fclose(file);
    return true;
}

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    node *ptr = table[first_hash(word)][second_hash(word)][third_hash(word)];

    while (ptr != NULL)
    {
        if (strcasecmp(word, ptr->word) == 0)
        {
            return true;
        }
        else
        {
            ptr = ptr->next;
        }
    }

    return false;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return COUNT;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            for (int k = 0; k < N; k++)
            {
                node *ptr = table[i][j][k];

                while (ptr != NULL)
                {
                    node *tmp = ptr;
                    ptr = ptr->next;
                    free(tmp);
                }
            }
        }
    }
    return true;
}
