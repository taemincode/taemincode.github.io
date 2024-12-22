from cs50 import get_string


def main():
    greeting = get_string("Greeting: ").lower()
    greeting = greeting.strip()

    if greeting[0:5] == 'hello':
        print("$0")
    elif greeting[0] == 'h':
        print("$20")
    else:
        print("$100")

    return


main()
