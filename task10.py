grade = int(input())

if 0 <= grade <=59:
    print(grade + ": " + "F")
elif 60 <= grade <=69:
    print(grade + ": " + "D")
elif 70 <= grade <= 79:
    print(grade + ": " + "C")
elif 80 <= grade <= 89:
    print(grade + ": " + "B")
elif 90 <= grade <= 100:
    print(grade + ": " + "A")
