class Student:
    def getData(self,name):
        self.name=name
    def displayStudent(self):
        print("name:",self.name)
class Test(Student):
    def getMarks(self,marks):
        self.marks=marks
    def displayMarks(self):
        print("total marks:",self.marks)
r=input("enter name:")
c=int(input("enter marks"))
print("result")
stud1=Test()
stud1.getData(r)
stud1.getMarks(c)
stud1.displayStudent()
stud1.displayMarks()
        
