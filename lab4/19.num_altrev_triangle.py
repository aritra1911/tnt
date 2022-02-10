
def num_altrev_triangle(n: int):
    for i in range(n):
        if i % 2 == 0:
            for j in range(1, i + 2):
                print(j, end=' ')
        else:
            for j in range(i + 1, 0, -1):
                print(j, end=' ')
        print()

def main():
    n = int(input("Enter no. of rows: "))
    num_altrev_triangle(n)

if __name__ == '__main__':
    main()
