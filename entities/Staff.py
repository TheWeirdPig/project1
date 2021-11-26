from entities.Employees import Employees
from entities.EPosition import EPosition


class Staff(Employees):
    __department = ""
    __position = EPosition.STAFF
    __workingDays = 0

    def __init__(self):
        super().__init__()

        # self.__department = ""
        # self.__position = EPosition.STAFF
        # self.__workingDays = 0
        # super().__init__()

    @property
    def position(self, position):
        if position not in EPosition:
            print("Wrong position")
        else:
            self.__position = position

    def getSalary(self):
        sal = self._Employees__salaryRatio * 730 + \
            self._Employees__allowance +\
            self.__workingDays * 30
        return str(sal)
        # self._Employees__allowance +

    @staticmethod
    def validatePosition(position):
        if position == EPosition.STAFF:
            return "STAFF"
        elif position == EPosition.VICE_HEAD:
            return "VICE HEAD"
        else:
            return "HEAD"

    def __str__(self):
        return self._Employees__name + ", " +\
            self.__department + ", " +\
            self.validatePosition(self.__position) + ", " +\
            str(self._Employees__salaryRatio) + ", " +\
            str(self._Employees__allowance) + ", " +\
            str(self.__workingDays) + ", " +\
            str(self.getSalary())
        # self.__position + ", " +\

    def getStr(self):
        return self._Employees__name + "," +\
            self.__department + "," +\
            self.validatePosition(self.__position) + "," +\
            str(self._Employees__salaryRatio) + "," +\
            str(self.__workingDays) + ","
