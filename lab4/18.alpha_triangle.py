
def alpha_triangle(n: int):
    for i in range(n):
        for j in range(i, -1, -1):
            print(chr(65 + j), end=' ')
        print()

def main():
    n = int(input("Enter no. of rows: "))
    alpha_triangle(n)

if __name__ == '__main__':
    main()

