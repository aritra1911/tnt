
def main():
    n = int(input("Enter a number: "))
    sum = 0

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            sum += j

    print(f"S = {sum}")

if __name__ == '__main__':
    main()

