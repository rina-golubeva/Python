#ex 1
def my_log(lst: list) -> list:
    import math
    lst_new=[]
    for item in lst:
        if item > 0:
            lst_new.append(math.log(item))
        else:
            lst_new.append(None)
    return lst_new

#ex 2
def srznach(lst: list):
    import random
    import statistics
    max_number = max(lst)
    min_number = min(lst)
    max_index = lst.index(max_number)
    min_index = lst.index(min_number)
    if min_index < max_index:
        return(statistics.mean(lst[min_index+1:max_index-1]))
    else:
        lst[min_index]=lst[max_index] = (min_number + max_number)/2
        return(lst[max_index:min_index])

#ex 3
summa = 0
count = 0
lst = [1, 5, 6.3, 6, None, 2.0, -4, None]
for item in lst:
    if item != None:
        summa += item
        count += 1
sr = summa/count
for i in range(len(lst)):
    if lst[i] == None:
        lst[i] = sr
print(lst, sr)   

#ex 4       
text = '''Call me Ishmael. Some years ago - never mind how long precisely - having
little or no money in my purse, and nothing particular to interest me
on shore, I thought I would sail about a little and see the watery part
of the world. It is a way I have of driving off the spleen, and regulating
the circulation. - Moby Dick'''
text = text.split("\n")
lst_new = [[0] for i in range(5)]
for j in range(5):
   text[j]=text[j].split()
for i in text:
    for j in text[i]:
        if len(j)<=3:
            del(text[i], j)
print(text)
