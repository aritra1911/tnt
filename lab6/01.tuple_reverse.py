def main():
    my_tuple = (4, 4, 3, 2, 5, 7, 8, 8, 8, 7)
    duplicates = list(set([
        item for item in my_tuple if my_tuple.count(item) > 1
    ]));
    duplicates.reverse()
    print(duplicates)

if __name__ == '__main__':
    main()
