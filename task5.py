any_list = [1,0,-1,-2,3,4,0,0,-4,-6,-8]

def count(any_list):
    pos = neg = zero = 0
    for i in any_list:
        if i > 0:
            pos += 1
        if i == 0:
            zero += 1
        if i < 0:
            neg += 1
    print(pos / len(any_list))
    print(neg / len(any_list)) 
    print(zero / len(any_list)) 
    
count(any_list)
