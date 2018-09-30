class Emp():

    def __init__(self,id,name,dept,sal):
        self.id = id
        self._name = name
        self._dept = dept
        self.__sal = sal

    def __str__(self):
        return str(self.id) + "," + self._name + "," + self._dept + "," + str(self.__sal)

emp_1 = Emp(101,'Ram','IT',15000)
print(emp_1)