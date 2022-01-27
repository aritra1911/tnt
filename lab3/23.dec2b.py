
def main():
    dec = int(input("Enter the decimal number: "))
    b = int(input("Enter the base: "))
    numb = ''

    while dec:
        digit = dec % b
        if digit > 9:
            numb = chr(65 + digit - 10) + numb
        else:
            numb = str(digit) + numb
        dec //= b;

    prefix = ""
    if b == 8: prefix = "0"
    elif b == 16: prefix = "0x"
    print(prefix + numb)

if __name__ == '__main__':
    main()

