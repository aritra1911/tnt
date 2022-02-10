
def equilateral(ch: str, n: int):
    for i in range(n):
        for sp in range(n - i - 1):
            print(end=' ')
        for j in range(i+1):
            print(ch, end=' ')
        print()

def main():
    n = int(input("Enter no. of rows: "))
    equilateral('*', n)

if __name__ == '__main__':
    main()

