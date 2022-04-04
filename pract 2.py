def simple_calculate(x):
    try:
        c = input("Введите числа: ")
        c0 = c.index(' ')
        c1, c2 = int(c[:c0]), int(c[c0+1:])
        o = input("Введите оператор: ")
        if o=="+":
            print("Результат: ", c1+c2)
        if o=="-":
            print("Результат: ", c1-c2)
        if o=="*":
            print("Результат: ", c1*c2)
        if o=="/":
            print("Результат: ", c1/c2)
    except ZeroDivisionError:
        print("Ошибка деления на нуль")
    except ValueError:
        print("Ошибка преобразования типа")

        
def temper(x):
    import requests
    import json
    import matplotlib.pyplot as plt
    import statistics
    response = requests.get('https://raw.githubusercontent.com/dm-fedorov/python3_intro/master/lesson_10/temper.stat')
    response = response.text.split()
    response = list(map(float, response))
    maxi = max(response)
    mini = min(response)
    sr = statistics.mean(response)
    x_coords=range(828)
    l_coords = response
    print("Максимум - ", maxi, "Минимум - ", mini)
    print("Среднее - ", sr, "Уникальных - ", len(l_coords))
    plt.plot(x_coords, l_coords)
    plt.show()

    
def normal(x):
    import requests
    response = requests.get('https://raw.githubusercontent.com/dm-fedorov/python3_intro/master/lesson_10/moby.txt')
    response = response.text.lower()
    intab = ".,?!:;-"
    outtab = ","
    trantab = str.maketrans(intab, outtab*len(intab))
    response = response.translate(trantab).replace(",","")
    response = response.replace(" ","\n")
    with open("moby_clean.txt", 'a') as output_file:
        output_file.write(response)

        
def repeat():
    with open("moby_clean.txt") as file:
        text = file.read()
    text = text.replace("\n", " ")
    words = text.split()
    unic_words = set(words)
    d = {}
    n = 0
    for i in unic_words:
       n = words.count(i)
       d.update({i : n})
    import collections
    d1 = {k: d[k] for k in sorted(d, key=d.get, reverse=True)}
    keys1 = list(d1.keys())
    d2 = {k: d[k] for k in sorted(d, key=d.get)}
    keys2 = list(d2.keys())
    print("most common: ", keys1[:5])
    print("most unique: ", keys2[:5])

    
def logi(text1, text2):
    words1 = text1.split()
    set1 = set(words1)
    words2 = text2.split()
    set2 = set(words2)
    print("unique common: ", set(set1 & set2))
    print("union: ", set1 | set2)

    
def magic():
    q = input("Your question: ")
    import random
    import requests
    response = requests.get('https://raw.githubusercontent.com/dm-fedorov/python_basic/master/data/responses.txt')
    response = response.text.split('\n')
    while q!="esc":
        print(random.choice(response))
        q = input("Your question: ")  

        
def chastota():
    import requests
    response = requests.get('http://dfedorov.spb.ru/python3/src/romeo.txt')
    response = response.text.lower().split()
    words = set(response)
    d = {}
    n = 0
    for i in words:
       n = response.count(i)
       d.update({i : n})
    print(d)
