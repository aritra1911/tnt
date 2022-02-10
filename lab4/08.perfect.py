
def sum_of_factors(n: int) -> int:
    sum = 1

    for i in range(2, n):
        if n % i == 0:
            sum += i

    return sum

def main():
    n = int(input("Enter a number: "))

    if n != 1 and n == sum_of_factors(n):
        print(n, "is a perfect number.")
    else:
        print(n, "is NOT a perfect number.")

if __name__ == '__main__':
    main()

