number = int(input())

final_hour = 0 + number // 60 %24
number %= 60

print(final_hour, number, sep = ":")
