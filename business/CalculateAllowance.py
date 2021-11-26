from entities.Staff import Staff
from entities.Teacher import Teacher
from entities.EDegree import EDegree
from entities.EPosition import EPosition


class CalculateAllowance():

    def calculateAllowance(emp):
        if type(emp) is Staff:
            if emp._Staff__position == EPosition.HEAD:
                return 2000
            elif emp._Staff__position == EPosition.VICE_HEAD:
                return 1000
            else:
                return 500
        elif type(emp) is Teacher:
            if emp._Teacher__degree == EDegree.BACHELOR:
                return 300
            elif emp._Teacher__degree == EDegree.MASTER:
                return 500
            else:
                return 1000
