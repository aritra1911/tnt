
def print_odds(start: int, end: int):
    print("Odds:")

    # Skip the first number if it isn't odd
    if not start & 1:
        start += 1

    for num in range(start, end + 1, 2):
        print(f"  {num}")

def print_evens(start: int, end: int):
    print("Evens:")

    # Skip the first number if it is odd
    if start & 1:
        start += 1

    for num in range(start, end + 1, 2):
        print(f"  {num}")

def main():
    start = int(input("Enter starting number: "))
    end = int(input("Enter where to terminate: "))
    print_odds(start, end)
    print() # A separator
    print_evens(start, end)

if __name__ == '__main__':
    main()

