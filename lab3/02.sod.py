
def main():
    n = int(input("Enter a number: "))
    sum = 0
    while n:
        sum += n % 10
        n //= 10

    print(f"Sum of digits : {sum}")

if __name__ == '__main__':
    main()

