from abc import abstractmethod


class Employees():
    def __init__(self):
        self.__name = ""
        self.__salaryRatio = 0
        self.__alowance = 0

    @abstractmethod
    def getSalary(self):
        pass
