
class Calculator:

    def userInput(self,no1,no2):
        self.no1 = no1
        self.no2 = no2


    def add(self):
        return self.no1+self.no2

    def sub(self):
        return self.no1-self.no2

    def mul(self):
        return self.no1*self.no2

    def div(self):
        return self.no1//self.no2


cal = Calculator()
cal.userInput(21,4)
print("sum is: ",cal.add())
print("subtraction is: ",cal.sub())
print("multiplication is: ",cal.mul())
print("division is: ",cal.div())

