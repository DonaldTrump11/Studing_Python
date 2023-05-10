# TODO: оптимизировать (сделать короче)
f = open('/home/alex/Рабочий стол/file.txt');
s = [val for val in f.read().split()]
f.close()

d = dict()
i = 1

for j in s :
    if j in d :
        d[j] += 1
    else :
        d[j] = 1

#  TODO: отсортировать по количеству вхождений
print('№ \t словосочетание \t количество повторений');
for key, value in sorted(d.items(), key=lambda x: -x[1]) :
    print('{:<5} {:<30} {:<3}'.format(i, key, value))
    i +=1

