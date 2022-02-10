
def is_prime(n: int) -> bool:
    if n == 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

def main():
    n = int(input("Enter a number: "))

    for i in range(3, n + 1):
        if is_prime(i):
            print(i, end=" ")

    print()

if __name__ == '__main__':
    main()

