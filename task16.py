a = "A"
b = "B"
c = "C"
packet = int(input())

if a in packet and b in packet:
    print("Yes")
elif a in packet and b in packet and c in packet:
    print("Yes")
elif a in packet and c in packet:
    print("Yes")
else:
    print("No")
