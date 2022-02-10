
from typing import List

def trial_division(n: int) -> List[int]:
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1: a.append(n)
    # Only odd number is possible
    return a

def prime_factors(n: int) -> List[int]:
    return list(set(trial_division(n)))

def main():
    n = int(input("Enter a number: "))
    print("Prime factors :", " ".join([ str(pf) for pf in prime_factors(n)]))

if __name__ == '__main__':
    main()

