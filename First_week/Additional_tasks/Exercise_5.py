
# Ввод в программу
strok = input()     # Вводим в программу строку, которую нужно расшифровать
slovar_ = input()   # Вводим алфавит для расшифровки

# Запишем в список латинский алфавит
slovar=[]
for i in range(97,123):
    slovar.append(chr(i))

# Запишем в список алфавит для расшифровки
slovar_1 = []
for i in slovar_ :
    slovar_1.append(i)

# Вывод работы программы
for j in strok: 
    try:                            # Выведем каждый элемент строки в расшифрованном виде
        a = slovar_1.index(j)
        print(slovar[a], end= "")
    except:                         # Выведем символы, которые расшифровывать не нужно
        print(j, end= "")
print("")


