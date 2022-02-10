
def next_fib(n):
    a = 0;
    b = 1;
    while n:
        yield b
        c = a + b
        a = b
        b = c
        n -= 1;

def main():
    n = int(input("Enter number of terms: "))
    for fib in next_fib(n):
        print(fib, end=' ')
    print()

if __name__ == '__main__':
    main()

