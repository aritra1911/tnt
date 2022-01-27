
def main():
    start = int(input("Enter starting number: "))
    end = int(input("Enter where to terminate: "))

    first_is_odd = False

    if start & 1:
        first_is_odd = True
        print("Odds:")
    else:
        print("Evens:")

    for i in range(start, end + 1, 2):
        print(f"  {i}")

    print()

    if first_is_odd:
        print("Evens:")
    else:
        print("Odds:")

    for i in range(start + 1, end + 1, 2):
        print(f"  {i}")

if __name__ == '__main__':
    main()

