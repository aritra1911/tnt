def main():
    my_tuple = (4, 4, 3, 2, 5, 7, 8, 8, 8, 7)
    evens = tuple([ item for item in my_tuple if item & 1 == 0 ])
    odds = tuple([ item for item in my_tuple if item & 1 == 1 ])
    print("Evens :", evens);
    print("Odds :", odds);

if __name__ == '__main__':
    main()
