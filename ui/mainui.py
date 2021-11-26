from business.EmployeeManagement import EmployeeManagement
from entities.EDegree import EDegree
from entities.Employees import Employees
from entities.Staff import Staff
from entities.Teacher import Teacher
from entities.EPosition import EPosition


def displayEmployees(lst):
    if lst:
        print("Name-------Fac/Dept--Deg/Pos--Sal Ratio--" +
              "Allowance--Hours/Days--Salary")
        for e in lst:
            print(e)


def addNewEmployee():
    empList = EmployeeManagement()
    opt = input(
        "Do you want to create a Staff or a Teacher (enter S for Staff, otherwise for Teacher)?: ")
    if opt == "s":
        newEmp = Staff()
        s = input("Name: ")
        newEmp._Employees__name = s
        s = input("Salary Ratio: ")
        newEmp._Employees__salaryRatio = int(s)
        s = input("Department: ")
        newEmp._Staff__department = s
        s = input("Position (1= HEAD, 2= VICE HEAD, 3= STAFF): ")
        while True:
            if s == "1":
                newEmp._Staff__position = EPosition.HEAD
                break
            elif s == "2":
                newEmp._Staff__position = EPosition.VICE_HEAD
                break
            elif s == "3":
                newEmp._Staff__position = EPosition.STAFF
                break
            else:
                print("Wrong position selection")
                s = input("Position (1= HEAD, 2= VICE HEAD, 3= STAFF): ")
        s = input("Number of working days: ")
        newEmp._Staff__workingDays = int(s)
        empList.createEmployee(newEmp)
        # empList.addEmployee(newEmp, f)
        # f.write(newEmp.getStr())
    elif opt == "t":
        newEmp = Teacher()
        s = input("Name: ")
        newEmp._Employees__name = s
        s = input("Salary Ratio: ")
        newEmp._Employees__salaryRatio = int(s)
        s = input("Faculty: ")
        newEmp._Teacher__faculty = s
        s = input("Degree (1= BACHELOR, 2= MASTER, 3= DOCTOR): ")
        while True:
            if s == "1":
                newEmp._Teacher__degree = EDegree.BACHELOR
                break
            elif s == "2":
                newEmp._Teacher__degree = EDegree.MASTER
                break
            elif s == "3":
                newEmp._Teacher__degree = EDegree.DOCTOR
                break
            else:
                print("Wrong position selection")
                s = input("Position (1= HEAD, 2= VICE HEAD, 3= STAFF): ")
        s = input("Number of teaching hours: ")
        newEmp._Teacher__teachingHours = int(s)
        empList.createEmployee(newEmp)
        # empList.addEmployee(newEmp, f)


def option():

    # with open('data.txt', 'rb') as f:
    #     for chunk in iter(lambda: f.readlines(), ''):
    #         empList.append(chunk)

    func = 0
    while func != 6:
        print("University Staff Management:")
        print("    1. Add Staff")
        print("    2. Search Staff by Name")
        print("    3. Search Staff by Department/Faculty")
        print("    4. Search Staff by Position/Degree")
        print("    5. Display all staff")
        print("    6. Exit")
        func = int(input("Select function: "))
        if func == 1:
            addNewEmployee()
        elif func == 2:
            empList = EmployeeManagement()
            lst = empList.getAllEmployees()
            name = input("Please input the name: ")
            lst2 = empList.getEmployeeByName(name)
            displayEmployees(lst2)
            input()
        elif func == 3:
            empList = EmployeeManagement()
            lst = empList.getAllEmployees()
            dof = input("Please input department or faculty: ")
            lst = empList.getEmployeeByDepartmentOrFaculty(dof)
            displayEmployees(lst)
            input()
        elif func == 4:
            # pod = input("Please input the position or degree: ")
            # lst = empList.getEmployeeByPositionOrDegree(pod)
            # displayEmployees(lst)
            input()
        elif func == 5:
            empList = EmployeeManagement()
            lst = empList.getAllEmployees()
            displayEmployees(lst)
            input()
