def read_employees(filename):
    employees = []
    with open(filename, 'r') as file:
        for line in file:
            name, age, dept, salary = line.strip().split(',')
            dict = { 'Name': name, 'Age': int(age), 'Department': dept, 'Salary': float(salary) }
            employees.append(dict)
    return employees

def filter_senior_employees(employees):
    seniors= list(filter(lambda emp: emp['Age'] > 30, employees))
    for emp in seniors:
          print(emp)

def apply_bonus(employees):
    bonus=list(map(lambda emp: { **emp, 'Salary': round(emp['Salary'] * 1.10, 2) }, employees))
    print("10% bonus applied to all employees.")
    for emp in bonus:
          print(emp)

def sort_by_salary(employees):
    sort=sorted(employees, key=lambda emp: emp['Salary'], reverse=True)
    for emp in sort:
          print(emp)

def write_high_earners(employees, filename='high_earners.txt'):
    high_earners = list(filter(lambda emp: emp['Salary'] > 60000, employees))
    with open(filename, 'w') as file:
        for emp in high_earners:
            file.write(f"{emp['Name']},{emp['Age']},{emp['Department']},{emp['Salary']}\n")
    print(f"High earners written to {filename}")

def main():
    filename = 'employees.txt'
    employees = read_employees(filename)
    while True:
        print("\nChoose from the below options:")
        print("1. View All Employees")
        print("2. View Employees Older Than 30")
        print("3. Apply 10% Bonus")
        print("4. View Sorted Employees by Salary")
        print("5. Save High Earners to File")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            for emp in employees:
                print(emp)
        elif choice == '2':
            filter_senior_employees(employees)
        elif choice == '3':
            apply_bonus(employees)
        elif choice == '4':
            sort_by_salary(employees)
        elif choice == '5':
            write_high_earners(employees)
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
main()
