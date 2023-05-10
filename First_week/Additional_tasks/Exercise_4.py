import random

# Введем значения в программу
k = int(input())    # Количество победителей
j = str(input()).split()    # Номер последнего билета и буквенный индекс всех билетов

# Запишем все номера билетов в список
spis = []
i = 0;
while i < int(j[0]) :
    spis.append([str(i+1).zfill(len(j[0])), j[1].upper()])     # запишем номер билета с нулями перед значимым числом и буквенный индекс заглавными буквами
    i = i + 1

# Выведем билеты-победители
m = k
c = int(j[0])
if k >= c :
    while c >0 :
        l = random.choice(spis)
        print(f'Победитель номер {c} - "{" ".join(l)}"')
        spis.remove(l)
        c -= 1
else: 
    while m>0 :
        l = random.choice(spis)
        print(f'Победитель номер {m} - "{" ".join(l)}"')
        spis.remove(l)
        m -= 1
