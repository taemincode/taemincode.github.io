from cs50 import get_string


def main():
    greeting = get_string("Greeting: ").lower()

    if 'hello' in greeting:
        print("$0")
    elif 'h' in greeting:
        print("$20")
    else:
        print("$100")

    return


main()
