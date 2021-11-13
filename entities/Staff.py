from entities.Employees import Employees
from entities.EPosition import EPosition


class Staff(Employees):
    def __init__(self):
        super().__init__()
        self.__department = ""
        self.__position = EPosition.STAFF
        self.__workingDays = 0

    @property
    def position(self, position):
        if position not in EPosition:
            print("Wrong position")
        else:
            self.__position = position

    def getSalary(self):
        sal = self.__salaryRatio * 730 + self.__allowance + self.__workingDays * 30
        return sal

    def toString(self):
        return super.__name + ", " +\
            super.__salaryRatio + ", " +\
            super.__allowance + ", " +\
            self.__department + ", " +\
            self.__position + ", " +\
            self.__workingDays
