
def sum_series(n: int) -> int:
    return sum([ sum(range(1, i + 1)) for i in range(1, n + 1)])

def main():
    n = int(input("Enter a number: "))
    print("S =", sum_series(n))

if __name__ == '__main__':
    main()

