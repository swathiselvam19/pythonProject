try:
    length = 10
    length/width
except NameError:
    print("variable has been used before defining it")
except ZeroDivisionError:
    print("Division by zero is invalid kindly change your input")