from pyfiglet import Figlet
import sys


def main()
    figlet = Figlet()
    figlet.getFonts()

    if len(sys.argv) == 2:
        if argv[1] not in ['-f', '--font']:
            print("Invailid usage")
            sys.exit

        figlet.setFont(font=sys.argv[3])
    elif len(sys.argv) == 0:
        figlet.setFont(font)
    else:
        print("Invalid usage")

    figlet.setFont(font=f)

    input = input("Input: ")
    print(f"Output:\n{figlet.renderText(input)}")
