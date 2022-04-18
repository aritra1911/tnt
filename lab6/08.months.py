def main():
    month_names = { 'January', 'February', 'March', 'April', 'May', 'June',
                    'July', 'August', 'September', 'October', 'November',
                    'December' }

    for i in range(len(month_names)):
        print(list(month_names)[len(month_names) - i - 1])

if __name__ == '__main__':
    main()
