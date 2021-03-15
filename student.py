class student:
    def __init__(self, name, dept, mark):
        self.name = name
        self.dept = dept
        self.mark = mark
    def displaystudent(self):
     print("name : ", self.name,   "dept: ", self.dept,   "mark: ", self.mark)

stud1 = student("Rinu", "MCA", 100 )
stud2 = student("Victer", "MCA", 100)
stud1.displaystudent()
stud2.displaystudent()