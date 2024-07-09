import math
a,b,c = int(input()),int(input()),int(input())

D = b**2 - 4*a*c

if D > 0:
    x1 = (-b + math.sqrt(D))/(2*a)
    x2 = (-b - math.sqrt(D))/(2*a)
    print(x1, x2)
elif D == 0:
    x = -b/(2*a)
    print(x)
else:
    print("No solutions")
