from pyfiglet import Figlet
import sys


def main()
    figlet = Figlet()
    figlet.getFonts()

    if len(sys.argv) == 2
    {
        if argv[1] not in ['-f', '--font']:
            print("Invailid usage")
            sys.exit

        figlet.setFont(font=sys.argv[3])
    }
    elif len(sys.argv) == 0
    {
        print("Invalid)
    }

    figlet.setFont(font=f)

    print(figlet.renderText(s))
