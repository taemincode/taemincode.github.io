from cs50 import get_string
from pyfiglet import Figlet
import sys


def main():
    figlet = Figlet()
    figlet.getFonts()

    if len(sys.argv) == 2:
        if argv[1] not in ['-f', '--font']:
            print("Invailid usage")
            sys.exit

        figlet.setFont(font=sys.argv[2])
    elif len(sys.argv) == 1:
        figlet.setFont(font=slant)
    else:
        print("Invalid usage")
        sys.exit

    input = get_string("Input: ")
    print(f"Output:\n{figlet.renderText(input)}")


main()
