from abc import abstractmethod


class Employees():

    __name = ""
    __salaryRatio = 0
    __allowance = 0

    def __init__(self):
        pass
        # self.__name = name
        # self.__salaryRatio = salaryRatio
        # self.__name = ""
        # self.__salaryRatio = 0
        # self.__allowance = 0

    @abstractmethod
    def getSalary(self):
        pass
