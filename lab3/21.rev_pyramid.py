def main():
    n = int(input("Enter no. of rows: "))
    row = list()
    for i in range(n + 1):
        l = len(row)
        new_row = list()
        for j in range(l):
            if j == 0:
                new_row.append(1)
            else:
                new_row.append(row[j] + row[j - 1])
        new_row.append(1)
        row = new_row
        for sp in range(n - i):
            print(" ", end="")
        for num in row:
            print(f"{num} ", end="")
        print()

if __name__ == '__main__':
    main()
