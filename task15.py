a, b, c = int(input()), int(input()), int(input())

if a < b + c and b < a + c and c < a + b:
    if a == b == c:
        print("Equilateral")
    elif (a == b and a != c) or (a == c and a != b) or (c == b and c != a):
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Invalid triangle")
