import math
a = int(input("Enter the number in front of the x square and press enter"))
b = int(input("Enter the number before x and press enter"))
c = int(input("Enter the third number and press enter" ))
d=(b*b)-(4*a*c)
if (d>0):
    xfirst=(-b+math.sqrt(d))/(2*a)
    xsecond=(-b-math.sqrt(d))/(2*a);
    print( "Two roots: " , xfirst , " " , xsecond)
elif (d==0):
    print( "One root: " , (-b-math.sqrt(d)/(2*a)))
else:
    print(" No roots")