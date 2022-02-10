
def kiitcsit():
    KIITCSIT = "KIITCSIT"
    n = len(KIITCSIT)
    for i in range(n):
        print(KIITCSIT[:n - i], end="")
        print("  " * i , end="")
        print(KIITCSIT[n - i - 1::-1], end="")
        print()
    for i in range(n - 1):
        print(KIITCSIT[:i + 2], end="")
        print("  " * (n - i - 2) , end="")
        print(KIITCSIT[i + 1::-1], end="")
        print()

def main():
    kiitcsit()

if __name__ == '__main__':
    main()

