class calc:
    num = 100

    def getdata(self, c, d):
        self.firastnumber = c
        self.secondnumber = d
        print("hi in a function")

    def summation(self):
        return self.firastnumber + self.secondnumber + calc.num

obj = calc()
obj.getdata(40, 40)
print(obj.summation())

obj1 = calc()
obj1.getdata(50, 50)
print(obj1.summation())
