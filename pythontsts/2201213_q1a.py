first=int(input("Enter number-1:"))
second=int(input("Enter number-2:"))
z=int(input("Enter a arithematic operator\n1.+\n2.-\n3.*\n4./"))
if z==1:
        print("x+y=",first+second)
elif z==2:
        print("x-y=",first-second)
elif z==3:
         print("x*y=",first*second)
elif z==4:
         print("x/y=",first/second)
else:
        print("Invalid operator")

