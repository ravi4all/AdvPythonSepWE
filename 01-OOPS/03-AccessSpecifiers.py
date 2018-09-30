# Private/Protected/Public
class Emp():

    def __init__(self,id,name,dept,sal):
        # Public Scope
        self.id = id
        # Protected Variables
        self._name = name
        self._dept = dept
        # Private Variable
        self.__sal = sal

    def showEmp(self):
        print("Id : {}".format(self.id))
        print("Name : {}".format(self._name))
        print("Dept : {}".format(self._dept))
        print("Sal : {}".format(self.__sal))

emp_1 = Emp(101,'Ram','IT',15000)
# emp_1.id = 101
# emp_1.name = 'Ram'
# emp_1.dept = 'IT'
# emp_1._name = 'Ram'
# emp_1._dept = 'IT'
# emp_1.sal = 15000
# print(emp_1._name)
# emp_1._name = 'Shyam'

# print(emp_1.__sal)
# emp_1.__sal = 25000

emp_1.showEmp()
print(emp_1.__dict__)