
def rev(num: int) -> int:
    rev = 0

    while num:
        rev = rev * 10 + num % 10
        num //= 10

    return rev

def main():
    n = int(input("Enter a number: "))
    print("Reverse :", rev(n))

if __name__ == '__main__':
    main()

