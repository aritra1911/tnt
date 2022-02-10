
def isosceles(ch: str, n: int):
    for i in range(n):
        for j in range(i+1):
            print(ch, end=' ')
        print()

def main():
    n = int(input("Enter no. of rows: "))
    isosceles('*', n)

if __name__ == '__main__':
    main()

