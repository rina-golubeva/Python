documents = [
 {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
 {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
 {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
 '1': ['2207 876234', '11-2'],
 '2': ['10006'],
 '3': []
}


def vladelez(x):
    nomer = input("Введите номер документа: ")
    k=0
    for doc in documents:
        if doc['number'] == nomer:
            k+=1
            print("Владелец документа: ", doc.get('name'))
    if k==0:
        print("Документ не найден в базе")


def polka(x):
    nomer = input("Введите номер документа: ")
    k=0
    for polka in directories:
        for doc in directories[polka]:
            if doc == nomer:
                k+=1
                print("Документ хранится на полке: ", polka)
    if k==0:
        print("Документ не найден в базе")


def information(x):
    for docum in documents:
        for polka in directories:
            for doc in directories[polka]:
                if doc == docum["number"]:
                    print("№: ", docum['number'], "тип: ", docum['type'], "владелец: ", docum['name'], "полка хранения: ", polka)


def new_polka(x):
    nomer = input("Введите номер полки: ")
    if nomer in directories:
        print("Такая полка уже существует. Текущий перечень полок: ", ", ".join(list(directories.keys())))
    else:
        directories[nomer]={}
        print("Полка добавлена. Текущий перечень полок: ", ", ".join(list(directories.keys())))


def delete_polka(x):
    nomer = input("Введите номер полки: ")
    if nomer in directories:
        if len(directories[nomer])==0:
            del directories[nomer]
            print("Полка удалена. Текущий перечень полок: ", ", ".join(list(directories.keys())))
        else:
            print("На полке есть документы, удалите их перед удалением полки.")
            print("Текущий перечень полок: ", ", ".join(list(directories.keys())))   
    else:
        print("Такой полки не существует. Текущий перечень полок: ", ", ".join(list(directories.keys())))


def add_doc(x):
    nomer = input("Введите номер документа: ")
    t = input("Введите тип документа: ")
    vlad = input("Введите владельца документа: ")
    polka = input("Введите полку для хранения: ")
    if polka in directories:
        b = {'type': t, 'number': nomer, 'name': vlad}
        documents.append(b)
        print("Документ добавлен. Текущий список документов: ")
        directories[polka].append(nomer)
    else:
        print("Такой полки не существует. Добавьте полку командой as.")
        print("Текущий список документов: ")
    for docum in documents:
        for polk in directories:
            for doc in directories[polk]:
                if doc == docum["number"]:
                    print("№: ", docum['number'], "тип: ", docum['type'], "владелец: ", docum['name'], "полка хранения: ", polka)        


def delite_doc(x):
    nomer = input("Введите номер документа: ")
    k=0
    for doc in documents:
        if doc['number'] == nomer:
            k+=1
            documents.remove(doc)
            for polka in directories:
                for docum in directories[polka]:
                    if nomer==docum:
                        directories[polka].remove(nomer)
            print("Документ удален. ")
    if k==0:
        print("Документ не найден в базе.")
    print("Текущий список документов: ")
    for docum in documents:
        for polka in directories:
            for doc in directories[polka]:
                if doc == docum["number"]:
                    print("№: ", docum['number'], "тип: ", docum['type'], "владелец: ", docum['name'], "полка хранения: ", polka)        


def throw(x):
    nomer = input("Введите номер документа: ")
    polka = input("Введите номер полки: ")
    if polka in directories:
        for polk in directories:
            for doc in directories[polk]:
                if doc == nomer:
                    directories[polk].remove(nomer)
        directories[polka].append(nomer)
        print("Документ перемещен. Текущий список документов: ")
        for docum in documents:
            for polka in directories:
                for doc in directories[polka]:
                    if doc == docum["number"]:
                        print("№: ", docum['number'], "тип: ", docum['type'], "владелец: ", docum['name'], "полка хранения: ", polka)        
    else:
        print("Такой полки не существует. Текущий перечень полок: ", ", ".join(list(directories.keys())))


inp = 0
while inp != "q":
    inp = input("Введите команду: ")
    if inp == "p":
        vladelez(inp)
    if inp == "s":
        polka(inp)
    if inp == "I":
        information(inp)
    if inp == "ads":
        new_polka(inp)
    if inp == "ds":
        delete_polka(inp)
    if inp == "ad":
        add_doc(inp)
    if inp == "d":
        delite_doc(inp)
    if inp == "m":
        throw(inp)      
