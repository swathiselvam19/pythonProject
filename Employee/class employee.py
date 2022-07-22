class Employee:
    def setnumberofworkinghours(self):
        self.numberofworkinghours = 40

    def displaythenumberworkinghours(self):
        print(self.numberofworkinghours)


class Trainee(Employee):
    def setnumberofworkinghours(self):
        self.numberofworkinghours = 45

employee = Employee()
employee.setnumberofworkinghours()
print("number of working hours of the employee:", end='')
employee.displaythenumberworkinghours()