x = int(input("Enter your number"))

strx = str(x)

if strx == strx[::-1]:
    print("This number is polindrome")
else:
    print("This number isn't polidrome")
