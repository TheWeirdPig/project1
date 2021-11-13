from entities.Employees import Employees
from entities.EDegree import EDegree


class Teacher(Employees):
    def __init__(self, faculty, degree):
        super().__init__()
        self.__faculty = faculty
        self.__degree = EDegree.MASTER
        self.__teachingHours = degree

    @property
    def degree(self, degree):
        if degree not in EDegree:
            print("Wrong degree")
        else:
            self.__degree = degree

    def getSalary(self):
        sal = self.__salaryRatio * 730 + self.__allowance + self.__teachingHours * 45
        return sal

    def toString(self):
        return self.__name + ", " +\
            self.__salaryRatio + ", " +\
            self.__allowance + ", " +\
            self.__faculty + ", " +\
            self.__degree + ", " +\
            self.__teachingHours
