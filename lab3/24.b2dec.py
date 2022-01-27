
def main():
    numb = input("Enter the number: ")
    b = int(input("Enter the base: "))
    dec = 0

    if numb.lower().startswith("0x"):
        numb = numb[2:]
        if b != 16: print("Oh, is it not base 16 ?")

    if numb.lower().startswith("0"):
        numb = numb[1:]
        if b != 8: print("Oh, is it not base 8 ?")

    pos = 0
    for digit in numb.upper()[::-1]:
        numeric_digit = (ord(digit) - 55) if digit.isalpha() else int(digit)
        dec += b**pos * numeric_digit
        pos += 1

    print(dec)

if __name__ == '__main__':
    main()

