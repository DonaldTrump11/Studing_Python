import sys
import os
import json
import tempfile



try :
    a = str(sys.argv[1])
except: 
    print("ошибка ввода")
try :
    b = str(sys.argv[2])
except :
    print("ошибка ввода")
try :
    c = str(sys.argv[3])
except :
    c = None
try :
    d = str(sys.argv[4])
except :
    d = None
    




# Вывод словаря из файла
def vivod() :
    with open("/home/alex/Рабочий стол/project_1/capitals.json", "r") as my_file:
        capitals_json = my_file.read()
    capitals = json.loads(capitals_json)
    return capitals



def vvod(key_, value_):
    with open("/home/alex/Рабочий стол/project_1/capitals.json", "r", encoding="utf-8") as my_file:
        capitals_json = my_file.read()      # записываем в переменную содержимое файла

    capitals_json_1 = json.loads(capitals_json)     # переводим содержимое в словарь

    if key_ in capitals_json_1 :            # Вписываем в словарь новые данные(в список) к старому ключу
        _value_ = [capitals_json_1[key_]]
        _value_.append(value_)
        capitals_json_1[key_] = _value_
    else :
        capitals_json_1[key_] = value_      # вписваем в словарь новые данные к новому ключу
    capitals_json = json.dumps(capitals_json_1)     # переводим словарь обратно

    with open("/home/alex/Рабочий стол/project_1/capitals.json", "w", encoding="utf-8") as my_file:
        my_file.write(capitals_json)        # перезаписываем дополненное содержимое в файл
    return None


if a == "--key" and c == "--values":
    vvod(b, d)
if a == "--key" and c == None:
    try:
        if type(vivod()[b]) == list:
            print(", ".join(vivod()[b]))
        else:
            print(vivod()[b])
    except:
        print(None)
