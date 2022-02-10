
def base2dec(num: str, base: int) -> int:

    if num.lower().startswith("0x"):
        num = num[2:]
        if base != 16:
            print("Oh, is it not base 16 ?")

    if num.lower().startswith("0"):
        num = num[1:]
        if base != 8:
            print("Oh, is it not base 8 ?")

    dec = 0
    pos = 0
    for digit in num.upper()[::-1]:
        numeric_digit: int = (ord(digit) - 55) if digit.isalpha() else int(digit)
        dec += base**pos * numeric_digit
        pos += 1

    return dec

def main():
    num = input("Enter the number: ")
    base = int(input("Enter the base: "))
    dec = base2dec(num, base)
    print(dec)

if __name__ == '__main__':
    main()

