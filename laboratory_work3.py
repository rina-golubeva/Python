def todo_list():
    import json
    print("Простой todo: ")
    print("   1. Добавить задачу.")
    print("   2. Вывести список задач.")
    print("   3. Выход.")
    n = int(input('Укажите число: '))
    while(n!=3):
        if n==1:
            task = input('Сформулируйте задачу: ')
            categ = input('Добавьте категорию к задаче: ')
            time = input('Добавьте время к задаче: ')
            zad= """Задача: {z} Категория: {c} Дата:  {t}"""
            ex = zad.replace('{z}', task)
            ex = ex.replace('{c}', categ)
            ex = ex.replace('{t}', time)
            with open('todo.json', 'w') as f:
                json.dump(ex, f)
        elif n==2:
            try:
                with open('todo.json') as f:
                    numbers = json.load(f)
                print(numbers)
            except Exception as e:
                print(e)
        else:
            print("Неверное обращение к todo")
        n = int(input('Укажите число: '))
    print('задачи сохранены в файл!')
