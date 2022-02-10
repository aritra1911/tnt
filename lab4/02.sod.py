
def sod(n: int) -> int:
    digit = n % 10
    return 0 if not n else digit + sod(n // 10)

def main():
    n = int(input("Enter a number: "))
    print("Sum of digits :", sod(n))

if __name__ == '__main__':
    main()

