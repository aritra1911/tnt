
def get_prefix(base: int) -> str:
    if base == 8: return "0"
    if base == 16: return "0x"
    return ""

def dec2base(dec: int, base: int) -> str:
    ret = ""

    while dec:
        digit = dec % base
        if digit > 9:
            ret = chr(65 + digit - 10) + ret
        else:
            ret = str(digit) + ret
        dec //= base;

    ret = get_prefix(base) + ret
    return ret

def main():
    dec = int(input("Enter the decimal number: "))
    base = int(input("Enter the base: "))
    print(dec2base(dec, base))

if __name__ == '__main__':
    main()

