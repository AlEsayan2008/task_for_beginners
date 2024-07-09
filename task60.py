a = input()
b = input()
c = input()
d = input()
e = input()
empty_llist = []
lsa = list(a)
lsb = list(b)
lsc = list(c)
lsd = list(d)
lse = list(e)

empty_llist.append(lsa+lsb+lsc+lsd+lse)
print(*empty_llist)
