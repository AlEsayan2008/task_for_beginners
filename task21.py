def duplicate_checker(lst):
    if len(lst) == len(set(lst)):
        return False
    else:
        return True

duplicate_checker([1,1,2,3,4,5])
