def main():
    days = { 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
             'Saturday', 'Sunday' }

    tmp = list(days); tmp.pop(1); days = set(tmp)
    print("After removing 2nd value :", days);
    tmp = list(days); tmp.pop(-2); days = set(tmp)
    print("After removing 2nd last value :", days);

if __name__ == '__main__':
    main()
