import employees as emps

def main():
    emps.populate_employees();
    emps.employees += [{
        'id': 7876,
        'name': 'Adams',
    },
    {
        'id': 7900,
        'name': 'James',
    },
    {
        'id': 7902,
        'name': 'Ford',
    },
    {
        'id': 7934,
        'name': 'Miller',
    },
    {
        'id': 7941,
        'name': 'Davolio',
    },]

    print("After adding 5 more employees:")
    for employee in emps.employees:
        print(employee);
    print();

    emps.employees = [
        employee
        for employee in emps.employees
        if employee['id'] != 7900 and employee['id'] != 7654
    ];

    print("After deleting 2 employees:")
    for employee in emps.employees:
        print(employee);

if __name__ == '__main__':
    main()
