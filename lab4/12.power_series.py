
def power_series(n):
    i = 1
    delta = 2

    while i <= n:
        yield i
        i += delta
        delta *= 2

def main():
    n = int(input("Enter a number: "))
    for term in power_series(n):
        print(term, end=' ')
    print()

if __name__ == '__main__':
    main()

