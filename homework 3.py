#Задача 5

import random

list_words = ['самовар', 'весна', 'лето']
word = random.choice(list_words)
lenght = len(word)
letter = random.randint(0, lenght - 1)
print(f"{word[:letter]}?{word[letter+1:]}")
polz = input("Введите букву: ")
if polz == word[letter]:
    print("Победа!")
else:
    print("Попробуйте в другой раз!")
    
    
#Задача 6

text = """В тот год осенняя погода
Стояла долго на дворе
Зимы ждала ждала природа
Снег выпал только в январе
На третье в ночь Проснувшись рано
В окно увидела Татьяна
Поутру побелевший двор
Куртины, кровли и забор
На стеклах легкие узоры
Деревья в зимнем серебре
Сорок веселых на дворе
И мягко устланные горы
Зимы блистательным ковром
Все ярко, все бело кругом"""

strochki = len(text.splitlines())
print(f"Количество строк {strochki}")
slowa = text.count(" ") + strochki
print(f"Количество слов {slowa}")
