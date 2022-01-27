
def main():
    n = int(input("Enter a number: "))
    i = 1
    delta = 2

    while i <= n:
        print(i, end=" ")
        i += delta
        delta *= 2

    print()

if __name__ == '__main__':
    main()

