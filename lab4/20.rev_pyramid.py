
def rev_pyramid(n: int):
    for i in range(n, 0, -1):
        for sp in range(n - i):
            print(end="    ")
        for j in range(1, i + 1):
            print(j, end=' ')
        for j in range(i - 1, 0, -1):
            print(j, end=' ')
        print()

def main():
    n = int(input("Enter no. of rows: "))
    rev_pyramid(n)

if __name__ == '__main__':
    main()

