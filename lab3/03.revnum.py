
def main():
    n = int(input("Enter a number: "))
    rev = 0
    while n:
        rev = rev * 10 + n % 10
        n //= 10

    print(f"Reverse : {rev}")

if __name__ == '__main__':
    main()

