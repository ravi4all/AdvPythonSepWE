class Student():
    # Constructor
    def __init__(self):
        self.s_marks = []
        self.s_grades = []
        print("Init Called...")

    def showStudent(self,name,marks,grades):
        self.s_marks.append(marks)
        self.s_grades.append(grades)
        print("Name : {}, Marks : {}, Grades : {}".format(name, self.s_marks, self.s_grades))

    # Destructor Function
    def __del__(self):
        print("Destructor Called...")

# This line will call init by default
s_1 = Student()
s_1.showStudent("Ram",80,'A')

del s_1     # will call __del__ by default

s_2 = Student()
s_2.showStudent("Raman",86,'A+')
s_2.showStudent("Raman",96,'A+')