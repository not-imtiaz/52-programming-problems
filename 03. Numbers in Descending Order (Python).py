def print_descending_numbers():
    numbers = list(range(1000, 0, -1))

    # Process the list in chunks of 5
    for i in range(0, len(numbers), 5):
        chunk = numbers[i:i+5]
        print("  ".join(map(str, chunk)))


if __name__ == "__main__":
    print_descending_numbers()
