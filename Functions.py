# functions
width = 35
length = 55
def computer(length,width):
 area = length*width
 print(area)
computer(35,55)

number = 1
for row in range(1,4):
    for column in range(1,4):
        print(number, end=' ')
        number = number + 1
    print()
