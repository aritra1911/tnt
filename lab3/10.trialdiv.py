
def main():
    n = int(input("Enter a number: "))

    a = []
    f = 2
    while n > 1:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 1

    for num in set(a):
        print(num)

if __name__ == '__main__':
    main()

