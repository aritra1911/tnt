
def is_prime(n: int) -> bool:
    if n == 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

def main():
    n = int(input("Enter a number: "))
    if is_prime(n):
        print(n, "is a prime number.")
    else:
        print(n, "is NOT a prime number.")

if __name__ == '__main__':
    main()

