# Ввод в программу строки и форматирование всех букв в нижний регистр
s = input().lower()
# Создадим пустое множество
mn = set()

# пройдемся по каждому символу строки
for i in s :
    if i.isalpha() : # если символ - это буква, добавим во множество
        mn.add(i)

# Выведем элементы множества алфовитном порядке
for x in sorted(mn) :
    print(x, end = "")
print("")
