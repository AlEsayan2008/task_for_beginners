ls = []

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
g = int(input())

ls.append(a)
ls.append(b)
ls.append(c)
ls.append(d)
ls.append(e)
ls.append(f)
ls.append(g)

del ls[0]
del ls[2]

print(ls)
