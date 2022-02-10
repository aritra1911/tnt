
def bin_triangle(n: int):
    for i in range(n):
        for j in range(i+1):
            print((i + j + 1) % 2, end=' ')
        print()

def main():
    n = int(input("Enter no. of rows: "))
    bin_triangle(n)

if __name__ == '__main__':
    main()
