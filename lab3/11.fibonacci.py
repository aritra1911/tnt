
def main():
    n = int(input("Enter a number: "))

    a = 0
    b = 1
    for _ in range(n):
        print(b)
        c = a + b
        a = b; b = c

if __name__ == '__main__':
    main()

