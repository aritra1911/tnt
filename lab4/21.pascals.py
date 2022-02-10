
from typing import List

def get_next_row(row: List[int]) -> List[int]:
    if not row:
        return [ 1, ]

    next_row = list()
    for j in range(len(row)):
        next_row.append(1 if not j else (row[j] + row[j - 1]))
    next_row.append(1)

    return next_row

def pascals_triangle(n: int):
    row = list()
    for i in range(n):
        row = get_next_row(row)
        for sp in range(n - i):
            print(end=' ')
        for num in row:
            print(num, end=' ')
        print()

def main():
    n = int(input("Enter no. of rows: "))
    pascals_triangle(n + 1)

if __name__ == '__main__':
    main()

