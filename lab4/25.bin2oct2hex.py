
def bin2oct(bin: str) -> str:

    bitmap = {
        "000": "0",
        "001": "1",
        "010": "2",
        "011": "3",
        "100": "4",
        "101": "5",
        "110": "6",
        "111": "7",
    }

    ret = "0"   # prefix

    # strip off leading zeros
    while bin.startswith("0"): bin = bin[1:]

    bin_aligned3 = bin

    # pad zeros at the begining such that the # of
    # bits in `bin_aligned3` is a multiple of 3.
    if len(bin) % 3 > 0 or len(bin) == 0:
        bin_aligned3 = "0"*(3 - len(bin) % 3) + bin

    while len(bin_aligned3):
        # Get decimal equivalent of first 3 bits
        ret += bitmap[bin_aligned3[:3]]

        # Drop those 3 bits from the front
        bin_aligned3 = bin_aligned3[3:]

    return ret

def bin2hex(bin: str) -> str:

    bitmap = {
        "0000": "0",
        "0001": "1",
        "0010": "2",
        "0011": "3",
        "0100": "4",
        "0101": "5",
        "0110": "6",
        "0111": "7",
        "1000": "8",
        "1001": "9",
        "1010": "A",
        "1011": "B",
        "1100": "C",
        "1101": "D",
        "1110": "E",
        "1111": "F",
    }

    ret = "0x"  # prefix

    # strip off leading zeros
    while bin.startswith("0"): bin = bin[1:]

    bin_aligned4 = bin

    # pad zeros at the begining such that the # of
    # bits in `bin_aligned4` is a multiple of 4.
    if len(bin) % 4 > 0 or len(bin) == 0:
        bin_aligned4 = "0"*(4 - len(bin) % 4) + bin

    while len(bin_aligned4):
        # Get decimal equivalent of the first 4 bits
        ret += bitmap[bin_aligned4[:4]]

        # Drop those 3 bits from the front
        bin_aligned4 = bin_aligned4[4:]

    return ret

def main():
    bin = input("Enter the number: ")
    print("Oct :", bin2oct(bin))
    print("Hex :", bin2hex(bin))

if __name__ == '__main__':
    main()

