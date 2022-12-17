#basic assignment of variable
fullname="John Doe"
print(fullname)

# Many Values to Multiple Variables
num1,num2,num3=1,2,3
print(num1,num2,num3)

#global variable
x=1

def func():
    #local variable
    x=2
    print(x)

func()
print(x)

