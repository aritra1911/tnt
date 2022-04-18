
# 2. Write a Python program to multiply all the odd items in a list.

def mult_odd(elems):
    if not elems: return 0;

    product = 1;
    for elem in elems:
        if elem & 1:
            product *= elem;

    return product;

def main():
    list2 = [ 7, 8, 9, 15, 36, 114 ]
    print("List :", list2);
    print("Product of elements :", mult_odd(list2));

if __name__ == '__main__':
    main()
