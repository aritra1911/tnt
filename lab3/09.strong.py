
def main():
    n = int(input("Enter a number: "))
    m = n
    sum = 0

    while n:
        f = 1
        for i in range(2, n%10 + 1):
            f *= i
        sum += f
        n //= 10;

    if m == sum:
        print(f"{m} is a strong number.")
    else:
        print(f"{m} is NOT a strong number.")

if __name__ == '__main__':
    main()

