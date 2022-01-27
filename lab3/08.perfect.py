
def main():
    n = int(input("Enter a number: "))
    sum = 1

    for i in range(2, n):
        if n % i == 0:
            sum += i

    if n == sum:
        print(f"{n} is a perfect number.")
    else:
        print(f"{n} is NOT a perfect number.")

if __name__ == '__main__':
    main()

