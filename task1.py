#Hackerrank problem 01:
def sum_of_list(arr):
    min_num = min(arr)
    max_num = max(arr)
    totalmax = 0
    totalmin = 0
    for sum_with_min_num in arr:
        if sum_with_min_num < max_num:
            totalmin += sum_with_min_num
    for sum_with_max_num in arr:
        if sum_with_max_num > min_num:
            totalmax += sum_with_max_num
    return str(totalmin) + " " + str(totalmax)
    
        
        arr = [10,20,30,40,50]
final_result = sum_of_list(arr)
print(final_result)
