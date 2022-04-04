def new_stud(surname, name):
    lines=[]
    stud = surname+' '+name
    with open('students.txt','r', encoding='utf8') as file:
        for line in file:
            lines.append(line.strip())
    lines.append(stud)
    lines.sort()
    
    with open('students.txt','w', encoding='utf8') as file:
        for line in lines:
            file.write(line+'\n')
    


def find_stud(surname, name=None):
    k=0
    with open('students.txt','r', encoding='utf8') as file:
        for line in file:
            if surname in line:
                k+=1
                if name==None:
                    print(line)
                else:
                    print("Студент находится в группе")
        if k==0:
            print("Студент не находится в группе")



def change(surname, name, new_surname=None, new_name=None):
    stud = surname+' '+name
    k=0
    with open('students.txt','r', encoding='utf8') as file:
        lines=file.readlines()
    for line in lines:
        if stud in line:
            k+=1
    if k>0:
        if new_surname==None:
            lines.remove(stud+'\n')
            new_student=surname+' '+new_name
            lines.append(new_student+'\n')
        else:
            lines.remove(stud+'\n')
            if new_name==None:
                new_student=new_surname+' '+name
                lines.append(new_student+'\n')
            else:
                new_student=new_surname+' '+new_name
                lines.append(new_student+'\n')
        lines.sort()
        with open('students.txt','w', encoding='utf8') as file:
            for line in lines:
                file.write(line)
    else:
        print('Студент не находится в данной группе')



def delete_stud(surname, name=None):
    k=0
    studs=[]
    with open('students.txt','r', encoding='utf8') as file:
        lines = file.readlines()
    if name!=None:
        k+=1
        stud=surname+' '+name
        with open('students.txt','w', encoding='utf8') as file:
            for line in lines:
                if line!=stud+'\n':
                    file.write(line)
                    k=-1
    else:
        for line in lines:
            if surname in line:
                k+=1
                studs.append(line)
                    
    if k==0:
        print("Студент не находится в группе")
    if k>1:
        print(studs)
        name = input("Введите имя: ")
        return delete_stud(surname, name)
    if k==1:
        with open('students.txt','w', encoding='utf8') as file:
            for line in lines:
                if not(surname in line):
                    file.write(line)
