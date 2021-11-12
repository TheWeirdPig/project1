

class Employees():
    def __init__(self, name, sal_rate, dep_fal, pos_deg):
        self.__name = name
        self.__sal_rate = sal_rate
        self.__dep_fal = dep_fal
        self.__pos_deg = pos_deg

    def __str__(self):
        return list(self.__name + self.__sal_rate + self.__dep_fal + self.__pos_deg)
