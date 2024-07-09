a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
g = float(input())
h = float(input())

ls = []
ls.append(a)
ls.append(b)
ls.append(c)
ls.append(d)
ls.append(e)
ls.append(f)
ls.append(g)
ls.append(h)
print(sum(ls))
del ls[7]
print(sum(ls))
del ls[6]
print(sum(ls))
del ls[5]
print(sum(ls))
del ls[4]
print(sum(ls))
del ls[3]
print(sum(ls))
del ls[2]
print(sum(ls))
del ls[1]
print(sum(ls))
