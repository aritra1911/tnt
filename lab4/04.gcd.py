
def gcd(m: int, n: int) -> int:
    if m < n:
        m, n = n, m
    r = m % n
    return n if not r else gcd(n, r)

def main():
    m = int(input("Enter first number: "))
    n = int(input("Enter second number: "))
    print("GCD :", gcd(m, n))

if __name__ == '__main__':
    main()

