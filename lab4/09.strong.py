
def fact(n: int) -> int:
    return 1 if n <= 1 else n * fact(n - 1)

def sof(n: int) -> int:
    digit = n % 10
    return 0 if not n else fact(digit) + sof(n // 10)

def main():
    n = int(input("Enter a number: "))
    if n == sof(n):
        print(n, "is a strong number.")
    else:
        print(n, "is NOT a strong number.")

if __name__ == '__main__':
    main()

