
def main():

    bin2oct = {
        "000": "0",
        "001": "1",
        "010": "2",
        "011": "3",
        "100": "4",
        "101": "5",
        "110": "6",
        "111": "7",
    }

    bin2hex = {
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

    bin = input("Enter the number: ")
    oct = "0"
    hex = "0x"
    bin_aligned3 = ""
    bin_aligned4 = ""

    while bin.startswith("0"):
        bin = bin[1:]

    if len(bin) % 3 > 0 or len(bin) == 0:
        bin_aligned3 = "0"*(3 - len(bin) % 3) + bin
    else:
        bin_aligned3 = bin

    if len(bin) % 4 > 0 or len(bin) == 0:
        bin_aligned4 = "0"*(4 - len(bin) % 4) + bin
    else:
        bin_aligned4 = bin

    while len(bin_aligned3):
        oct += bin2oct[bin_aligned3[:3]]
        bin_aligned3 = bin_aligned3[3:]

    while len(bin_aligned4):
        hex += bin2hex[bin_aligned4[:4]]
        bin_aligned4 = bin_aligned4[4:]

    print("Oct : " + oct)
    print("Hex : " + hex)

if __name__ == '__main__':
    main()

