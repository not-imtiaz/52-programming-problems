def print_squares():
    try:
        n = int(input())

        while n > 0:
            h = int(input())

            for i in range(h):
                print("*" * h)

            if n > 1:
                print()

            n -= 1

    except (EOFError, ValueError):
        pass


if __name__ == "__main__":
    print_squares()
