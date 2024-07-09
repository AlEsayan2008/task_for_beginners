
import math

n = int(input())
params = []
for _ in range(n):
    h, r = int(input()), int(input())
    params.append({
        "h": h,
        "r": r
    })


def calculate(p1, p2):
    print(math.pi * p2 ** 2 * p1)


for item in params:
    calculate(p1=item["h"], p2=item["r"])
