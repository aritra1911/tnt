def main():
    n = int(input("Enter no. of rows: "))
    for i in range(n, 0, -1):
        for sp in range(n - i):
            print(f"    ", end="")
        for j in range(1, i + 1):
            print(f"{j} ", end="")
        for j in range(i - 1, 0, -1):
            print(f"{j} ", end="")
        print()

if __name__ == '__main__':
    main()
