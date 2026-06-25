def find_divisors():
    try:
        t = int(input())
    except EOFError:
        return

    for i in range(1, t + 1):
        try:
            n = int(input())
        except EOFError:
            break

        print(f"Case {i}:", end="")

        for j in range(1, n + 1):
            if n % j == 0:
                print(f" {j}", end="")

        print()


if __name__ == "__main__":
    find_divisors()
