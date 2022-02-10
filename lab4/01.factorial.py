
def fact(n: int) -> int:
    return 1 if n <= 1 else n * fact(n - 1)

def main():
    n = int(input("Enter a number: "))
    print("Factorial :", fact(n))

if __name__ == '__main__':
    main()

