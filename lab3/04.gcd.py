
def main():
    m = int(input("Enter first number: "))
    n = int(input("Enter second number: "))

    while True:
        if m < n: m, n = n, m
        r = m % n
        if r == 0: break
        m = n; n = r

    print(f"GCD : {n}")

if __name__ == '__main__':
    main()

