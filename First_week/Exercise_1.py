str_1 = str(input())
str_2 = str(input())
spis = []
out = dict()

for i in ''.join(filter(str.islower, str_2.lower())) :
    if i in out:
         continue
    for j in range(len(str_1)) :
        if i == str_1.lower()[j] :
            spis.append(j+1)
    if len(spis) == 0 :
        out[i] = None
        continue
    key, value = i, spis.copy()
    out.update({key: value})
    spis.clear()

for key, value in out.items() :
    print(key, end = " ");
    try:
        for x in value :
            print(x, end = " ")
        print("")
    except :
        print(value)

