def rectangle(m, n):
    for i in range(m):
        if i == 0:
            print("############")
        elif i == m - 1:
            print("############")
        else:
            print("#" + (n - 2) * " " + "#")


for _ in range(3):
    rectangle(10, 12)
