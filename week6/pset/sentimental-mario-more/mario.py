from cs50 import get_int


def main():
    while True:
        height = get_int("Height: ")
        if height > 0 and height < 9:
            break
    for i in range(height):
        row(height - (i + 1), i + 1)
        print("")


def row(space, brick):
    for i in range(space):
        print(" ", end="")
    brick_f(brick)
    print("  ", end="")
    brick_f(brick)


def brick_f(number_of_bricks):
    for i in range(number_of_bricks):
        print("#", end="")


main()
