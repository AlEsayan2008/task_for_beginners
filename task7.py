grades = [24,60,87,100,99]

def gradecounter(grades):
    res = []
    for grade in grades:
        if grade >= 40:
            mod5 = grade % 5
            if mod5 >= 3:
                grade += (5 - mod5)
            res.append(grade)
    return res

gradecounter(grades)
