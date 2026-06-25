import sys


def main():
    try:
        n = int(input())
        for _ in range(n):
            num_str = input()
            num = int(num_str)

            first = num % 10

            temp_num = num
            while temp_num >= 10:
                temp_num //= 10
            last = temp_num

            print(f"Sum = {first + last}")
    except (EOFError, ValueError):
        pass


if __name__ == "__main__":
    main()
