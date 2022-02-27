#exercize 1
import random
rand_number = random.randint(1,10)
polz_number = 0
while rand_number!=polz_number:
    polz_number = int(input("Попробуйте угадать число: "))
    if rand_number>polz_number:
        print("Введённое Вами число меньше загаданного")
    elif rand_number<polz_number:
        print("Введённое Вами число больше загаданного")
print(f"Верно! Выбранное число: {rand_number}")


#exercize 2
def new_password(a)->str:
    import random
    password_lenght = random.randint(7,10)
    password = []
    for i in range(1, password_lenght+1):
        password += chr(random.randint(33,126))
    password="".join(password)
    return password


#exercize 3
def check_password(password: str)->bool:
    password_lenght = len(password)
    
    def count_lower_upper(s: str):
        sum_upper=0
        sum_lower=0
        sum_number=0
        for i in s:
            if (i.isupper()):
                sum_upper+=1
            elif (i.islower()):
                sum_lower+=1
            elif (i.isdigit()):
                sum_number+=1
        return sum_upper, sum_lower, sum_number

    prov = count_lower_upper(password)

    if password_lenght >= 8 and prov[0]>=1 and prov[1]>=1 and prov[2]>=1:
        return True
    else:
        return False


#exercize 4
safe = False
pop = 0
while safe!=True:
    new = new_password(8)
    if check_password(new)!=True:
        pop+=1
    else:
        safe = True
        print(f"Password: {new}")
        print(f"Attempt: {pop}")
