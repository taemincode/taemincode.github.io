from cs50 import get_string


def main():
    # Prompt the user for some text
    text = get_string("Text: ")

    # Count the number of letters, words, and sentences in the text
    letters = 0
    words = 1
    sentences = 0
    for i in range(len(text)):
        if 'A' <= text[i] and text[i] <= 'Z' or 'a' <= text[i] and text[i] <= 'z':
            letters += 1
        elif text[i] == ' ':
            words += 1
        elif text[i] == '.' or text[i] == '!' or text[i] == '?':
            sentences += 1

    l = letters / words * 100
    s = sentences / words * 100;

    index = 0.0588 * l - 0.296 * s - 15.8

    if index >= 1 and index < 16:
        print(f"Grade {round(index)}")
    elif index >= 16:
        print("Grade 16+")
    else:
        print("Before Grade 1")


main()
