hour = int(input())
minute = int(input())
stuck = int(input())
sum_min = 60*hour+minute+stuck
print(sum_min//60%24, sum_min%60, sep = ":")
