# 1. greater among 4 number 
a = int(input("Enter 1st Number : "))
b = int(input("Enter 2nd Number : "))
c = int(input("Enter 3rd Number : "))
d = int(input("Enter 4th Number : "))

if(a>b and a>c and a>d):
    print("A is the greater number")
elif(b>a and b>c and b>d):
    print("B is the greater number")
elif(c>a and c>b and c>d):
    print("C is the greater number")
else:
    print("D is the greater number")