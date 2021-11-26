from entities.EDegree import EDegree
from entities.EPosition import EPosition
from entities.Employees import Employees
from business.CalculateAllowance import CalculateAllowance

from entities.Staff import Staff
from entities.Teacher import Teacher


def keyFunc(e):
    return e._Employees__name


class EmployeeManagement():
    def __init__(self):
        self.__empList = []

    # def addEmployee(self, newEmp):
    #     allowance = CalculateAllowance.calculateAllowance(newEmp)
    #     newEmp._Employees__allowance = allowance
    #     self.__empList.append(newEmp)

    def createEmployee(self, newEmp):
        allowance = CalculateAllowance.calculateAllowance(newEmp)
        newEmp._Employees__allowance = allowance
        with open("data.txt", "a") as f:
            f.write(newEmp.getStr())
            f.write('\n')

    def updateEmployeeInformation(emp):
        pass

    def deleteEmployee(emp):
        pass

    def getAllEmployees(self):
        # self.quickSort(self.__empList, 0, )
        with open("data.txt", "r") as f:
            for l in f:
                temp = l.split(",")
                if self.validateEmployeeType(temp[2]) == Teacher:
                    emp = Teacher()
                    emp._Employees__name = temp[0]
                    emp._Teacher__faculty = temp[1]
                    emp._Teacher__position = self.categorizeEmployeeType(
                        temp[2])
                    emp._Employees__allowance = CalculateAllowance.calculateAllowance(
                        emp)
                    emp._Employees__salaryRatio = float(temp[3])
                    emp._Teacher__teachingHours = float(temp[4])
                    self.__empList.append(emp)
                elif self.validateEmployeeType(temp[2]) == Staff:
                    emp = Staff()
                    emp._Employees__name = temp[0]
                    emp._Staff__department = temp[1]
                    emp._Staff__degree = self.categorizeEmployeeType(temp[2])
                    emp._Employees__allowance = CalculateAllowance.calculateAllowance(
                        emp)
                    emp._Employees__salaryRatio = float(temp[3])
                    emp._Staff__workingDays = float(temp[4])
                    self.__empList.append(emp)
        self.__empList.sort(key=keyFunc)
        return self.__empList

    def getEmployeeByName(self, name):
        lst = []
        for e in self.__empList:
            if e._Employees__name.find(name) > -1:
                lst.append(e)
        if lst:
            return lst
        else:
            print("Item not found")

    def getEmployeeByDepartmentOrFaculty(self, dof):
        lst = []
        for e in self.__empList:
            if type(e) is Staff:
                if e._Staff__department.find(dof) > -1:
                    lst.append(e)
            elif type(e) is Teacher:
                if e._Teacher__faculty.find(dof) > -1:
                    lst.append(e)
        if lst:
            return lst
        else:
            print("Item not found")

    # def getEmployeeByPositionOrDegree(self, pod):
    #     lst = []
    #     for e in self.__empList:
    #         if type(e) is Staff:
    #             if e._Staff__position.find(pod) > -1:
    #                 lst.append(e)
    #         elif type(e) is Teacher:
    #             if e._Teacher__degree.find(pod) > -1:
    #                 lst.append(e)
    #     if lst:
    #         return lst
    #     else:
    #         print("Item not found")

    def getEmployeeBySalary(self):
        pass

    @staticmethod
    def validateEmployeeType(tpe):
        if tpe in ("BACHELOR", "MASTER", "DOCTOR"):
            return Teacher
        elif tpe in ("STAFF", "VICE HEAD", "HEAD"):
            return Staff

    @staticmethod
    def categorizeEmployeeType(tpe):
        if tpe == "BACHELOR":
            return EDegree.BACHELOR
        elif tpe == "MASTER":
            return EDegree.MASTER
        elif tpe == "DOCTOR":
            return EDegree.DOCTOR
        elif tpe == "STAFF":
            return EPosition.STAFF
        elif tpe == "VICE HEAD":
            return EPosition.VICE_HEAD
        elif tpe == "HEAD":
            return EPosition.HEAD
