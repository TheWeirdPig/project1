
from entities.Employees import Employees
from entities.EPosition import EPosition


def displayStaff():
    employee = Employees("Tran Duc Manh", 0.5, 'IT', EPosition.STAFF)
    print("Name----------------Fac/Dept------Deg/Pos-----Sal Ratio----Allowance-----Hours/Days-----Salary")
    str = ("{}       {}      {}    {}").format(employee._Employees__name,
                                               employee._Employees__dep_fal,
                                               employee._Employees__pos_deg,
                                               employee._Employees__sal_rate)
    print(str)


def main():
    func = 0
    while func != 5:
        print("University Staff Management:")
        print("    1. Add Staff")
        print("    2. Search Staff by Name")
        print("    3. Search Staff by Department/Faculty")
        print("    4. Display Staff by Department/Faculty")
        print("    5. Exit")
        func = int(input("Select function: "))
        if func == 4:
            displayStaff()


if __name__ == "__main__":
    main()
