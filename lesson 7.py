#ex 1 
students = ["Вася", "Маша", "Петя", "Дима", "Марина", "Люба", "Коля", "Ваня"]
grades = {"Вася" : 4, "Петя" : 9, "Марина" : 8, "Люба" : 4, "Коля" : 5, "Ваня": 10}
for stud in students:
    print(stud, grades.get(stud, 'Контрольную работу не писал'))

for stud in grades:
    if grades[stud]>=8:
        print(stud)

good=[]
bad=[]
for stud in grades:
    if grades[stud]>=5:
        good.append(stud)
    else:
        bad.append(stud)
print(f"Хорошие и отличные оценки получили: {good}")
print(f"Удовлетворительные и плохие оценки получили: {bad}")


#ex 2
marks = {'Mary' : [5, 8, 9, 10, 3, 5, 6, 6],
        'John' : [3, 3, 6, 8, 2, 1, 8, 5],
        'Alex' : [4, 4, 7, 4, 7, 3, 2, 9],
        'Patricia' : [2, 1, 6, 8, 2, 3, 7, 4]}

course = int(input())

count = 0
summa = 0

for stud in marks:
    if marks[stud][0] == course:
        summa = sum(marks[stud][1:])
        count +=1

print(round(summa/count, 0)) 


#ex  3
marks = {'Mary' : [5, 8, 9, 10, 3, 5, 6, 6],
        'John' : [3, 3, 6, 8, 2, 1, 8, 5],
        'Alex' : [4, 4, 7, 4, 7, 3, 2, 9],
        'Patricia' : [2, 1, 6, 8, 2, 3, 7, 4]}

categories = {'отлично' : [8, 9, 10],
             'хорошо' : [6, 7],
             'удовлетворительно' : [4, 5],
             'неуд' : [0, 1, 2, 3]}

course = int(input())

count = 0
summa = 0

import statistics
for stud in marks:
    if marks[stud][0] == course:
        summa = statistics.mean(marks[stud][1:])
        count += 1

oz = round(summa/count, 0)
for cat in categories:
    if oz in categories[cat] :
        print (cat)
        
        
#ex 4

marks = {'Mary' : [5, 8, 9, 10, 3, 5, 6, 6],
        'John' : [3, 3, 6, 8, 2, 1, 8, 5],
        'Alex' : [4, 4, 7, 4, 7, 3, 2, 9],
        'Patricia' : [2, 1, 6, 8, 2, 3, 7, 4]}

oz= int(input())

count = 0

for stud in marks:
    for item in marks[stud]:
        if item >= oz:
            count+=1
print(count)
