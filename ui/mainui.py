from business.EmployeeManagement import EmployeeManagement
from entities.Employees import Employees
from entities.Staff import Staff
from entities.EPosition import EPosition


def displayStaff():
    employee = Employees("Tran Duc Manh", 0.5, 'IT', EPosition.STAFF)
    print("Name----------------Fac/Dept------Deg/Pos-----Sal Ratio----Allowance-----Hours/Days-----Salary")
    str = ("{}       {}      {}    {}").format(employee._Employees__name,
                                               employee._Employees__dep_fal,
                                               employee._Employees__pos_deg,
                                               employee._Employees__sal_rate)
    print(str)


def addNewEmployee(empList):
    opt = input(
        "Do you want to create a Staff or a Teacher (enter S for Staff, otherwise for Teacher)?: ")
    if opt == "s":
        newEmp = Staff()
        s = input("Name: ")
        newEmp.__name = s
        s = input("Salary Ratio: ")
        newEmp.__salaryRation = s
        s = input("Department: ")
        newEmp.__department = s
        s = input("Position (1= HEAD, 2= VICE HEAD, 3= STAFF): ")
        while True:
            if s == "1":
                newEmp.__position = EPosition.HEAD
                break
            elif s == "2":
                newEmp.__position = EPosition.VICE_HEAD
                break
            elif s == "3":
                newEmp.__position = EPosition.STAFF
                break
            else:
                print("Wrong position selection")
        s = input("Number of working days: ")
        newEmp.__workingDays = int(s)
    empList.addEmployee(newEmp)


def option():
    func = 0
    empList = EmployeeManagement()
    while func != 5:
        print("University Staff Management:")
        print("    1. Add Staff")
        print("    2. Search Staff by Name")
        print("    3. Search Staff by Department/Faculty")
        print("    4. Display Staff by Department/Faculty")
        print("    5. Exit")
        func = int(input("Select function: "))
        if func == 1:
            addNewEmployee(empList)
        elif func == 4:
            empList.displayAllEmployees()
