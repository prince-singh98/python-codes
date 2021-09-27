class Student:

    def studentInp(self,name,mark1,mark2):
        self.name=name
        self.mark1=mark1
        self.mark2=mark2

    def total(self):
        return self.mark1+self.mark2

    def studName(self):
        return self.name


stud=Student()

stud.studentInp("sumit",56,67)
print("Name : ",stud.studName())
print("total:",stud.total())