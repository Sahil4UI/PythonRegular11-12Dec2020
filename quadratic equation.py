import math
print("Coefficients of a quadratic equation- a*(x**2) + b*x + c ")
a= int(input("Enter value of a:- "))
b= int(input("Enter value of b:- "))
c= int(input("Enter value of c:- "))
D= (b**2) - 4*a*c
if D<0:
    print("Roots are complex")
    print(-b/(2*a),"+",math.sqrt(math.fabs(D)),"i")
    print(-b/(2*a),"-",math.sqrt(math.fabs(D)),"i")
elif D == 0:
    x= (-b) / (2*a)
    y= (-b) / (2*a)
    print(" The roots of a quadratic equation are: ", x,y)
elif D>0:
    x= (-b + math.sqrt(D)) / (2*a)
    y= (-b - math.sqrt(D)) /(2*a)
    
