import random

# Введем значения в программу
k = int(input())    # Количество победителей
j = str(input()).split()    # Номер последнего билета и буквенный индекс всех билетов


# Найдем номера билетов-победителей рандомным образом

m = 0;
mnog = []
if int(j[0]) > k:           # Запишем "k" номеров билетов-победителей в список
    while len(mnog) < k :
        l = random.randint(1, int(j[0]))
        if l in mnog :
            continue
        else :
            mnog.append(l)
else :                      # Если билетов меньше количества победителей, запишем в список все номера билетов
    while len(mnog) < int(j[0]) :
        l = random.randint(1, int(j[0]))
        if l in mnog :
            continue
        else :
            mnog.append(l)

# Вывод работы программы

i = 0
if int(j[0]) > k :
    while i < k :
        print(f'Победитель номер {i+1} - "{str(mnog[i]).zfill(len(j[0]))} {j[1].upper()}"')
        i = i+ 1
else :
    while i < int(j[0]) :
        print(f'Победитель номер {i+1} - "{str(mnog[i]).zfill(len(j[0]))} {j[1].upper()}"')
        i += 1;
