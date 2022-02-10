
def exponent(a: int, b: int) -> int:
    """Returns a ^ b"""
    return a ** b

def main():
    x = int(input("Enter x: "))
    n = int(input("Enter n: "))
    print("y =", exponent(x, n))

if __name__ == '__main__':
    main()

