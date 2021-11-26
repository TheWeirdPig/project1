from entities.Employees import Employees
from entities.EDegree import EDegree


class Teacher(Employees):
    __faculty = ""
    __degree = EDegree.BACHELOR
    __teachingHours = 0

    def __init__(self):
        super().__init__()

        # self.__faculty = faculty
        # self.__degree = EDegree.MASTER
        # self.__teachingHours = degree

    @property
    def degree(self, degree):
        if degree not in EDegree:
            print("Wrong degree")
        else:
            self.__degree = degree

    def getSalary(self):
        sal = self._Employees__salaryRatio * 730 + \
            self._Employees__allowance +\
            self.__teachingHours * 45
        return str(sal)

    @staticmethod
    def validateDegree(degree):
        if degree == EDegree.BACHELOR:
            return "BACHELOR"
        elif degree == EDegree.MASTER:
            return "MASTER"
        else:
            return "DOCTOR"

    def __str__(self):
        return self._Employees__name + ", " +\
            self.__faculty + ", " +\
            self.validateDegree(self.__degree) + ", " +\
            str(self._Employees__salaryRatio) + ", " +\
            str(self._Employees__allowance) + ", " +\
            str(self.__teachingHours) + ", " +\
            self.getSalary()
        # self.__degree + ", " +\

    def getStr(self):
        return self._Employees__name + "," +\
            self.__faculty + "," +\
            self.validateDegree(self.__degree) + "," +\
            str(self._Employees__salaryRatio) + "," +\
            str(self.__teachingHours) + ","
