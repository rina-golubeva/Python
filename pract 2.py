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
