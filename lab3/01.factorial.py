
def main():
    n = int(input("Enter a number: "))
    f = 1
    for i in range(2, n+1):
        f *= i

    print(f"Factorial : {f}")

if __name__ == '__main__':
    main()

