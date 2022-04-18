employees = list()

def populate_employees():
    global employees
    employees = [{
        'id': 7369,
        'name': 'Smith',
    },
    {
        'id': 7499,
        'name': 'Allen',
    },
    {
        'id': 7521,
        'name': 'Ward',
    },
    {
        'id': 7566,
        'name': 'Jones',
    },
    {
        'id': 7654,
        'name': 'Martin',
    },
    {
        'id': 7698,
        'name': 'Blake',
    },
    {
        'id': 7782,
        'name': 'Clark',
    },
    {
        'id': 7788,
        'name': 'Scott',
    },
    {
        'id': 7839,
        'name': 'King',
    },
    {
        'id': 7844,
        'name': 'Turner',
    },]

def main():
    populate_employees();
    for employee in employees:
        print(employee);

if __name__ == '__main__':
    main()
