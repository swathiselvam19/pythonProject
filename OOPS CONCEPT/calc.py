class calc:
    num = 100

    def getdata(self, c, d):
        self.firastnumber = c
        self.secondnumber = d
        print("hi in a function")

    def summation(self):
        return self.firastnumber + self.secondnumber + self.thirdnumber + self.fourthnumber + calc.num

    def __init__(self,a,b):
        self.thirdnumber = a
        self.fourthnumber = b
        print("i am running first")

obj = calc(20,20)
obj.getdata(40, 40)
print(obj.summation())

obj1 = calc(20,20)
obj1.getdata(50, 50)
print(obj1.summation())

#obj = calc(20,20)
#obj.getdata(40, 40)
#print(obj.summation())

#obj1 = calc(20,20)
#obj1.getdata(50, 50)
#print(obj1.summation())