
def main():
    n = int(input("Enter a number: "))

    if n == 1:
        print(f"{n} is NOT a prime number.")
        return

    for i in range(2, n):
        if n % i == 0:
            print(f"{n} is NOT a prime number.")
            return

    print(f"{n} is a prime number.")

if __name__ == '__main__':
    main()

