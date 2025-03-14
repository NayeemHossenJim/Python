# 1. Greatest between three number 
def greatest(a,b,c):
    if(a>b and a>c):
        print(f"The greatest number is : {a}")
    elif(b>a and b>c):
        print(f"The greatest number is : {b}")
    else:
        print(f"The greatest number is : {c}")
greatest(12,25,45)