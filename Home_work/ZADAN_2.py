f = open('/home/alex/Рабочий стол/file.txt');
s = [str(i) for i in f.read().split()]
f.close()
d = dict();
mn = s.copy()
x = 1

# TODO: Сделать один цикл из двух (т.е. только один проход по всем элементам)
for j in range(len(s)):
    try :
        mn[j] = s[j] + ' ' + s[j+1]
    except :
        mn[j] = s[j] + ' ' + s[0]

    if mn[j] in d :
        d[mn[j]] += 1
    else :
        d[mn[j]] = 1



print('№ \t словосочетание \t количество повторений');
for key, value in sorted(d.items(), key=lambda x: -x[1]) :
    print('{:<5} {:<30} {:<3}'.format(x, key, value))
    x += 1;
