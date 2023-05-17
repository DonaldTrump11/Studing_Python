def gen_series(series):
    """
    генератор серий лотерейных билетов, входные параметры: series -  - номер серии,
    выход - строка, состоящая из двух заглавных букв латинского алфавита
    """
    a=0
    for i in range(ord(series[0].lower()), 123):
        if a ==0 :
            a = 1
            for j in range(ord(series[1].lower()), 123) :
                s = (chr(i)+chr(j)).upper()
                yield s
        else: 
            for j in range(97,123) :
                s = (chr(i)+chr(j)).upper()
                yield s


def gen_number(length=6):
    """
    генератор номеров лотерейных билетов в одной серии, входные параметры:
    необязательный аргумент length - количество цифр в номере, по умолчанию равен 6
    """
    all_tickets = []
    for i in range(1, 10**length) :
        yield(str(i).zfill(length))
        

def gen_ticket_number(count, series, length=6):
    """
    генератор номеров билетов, входные параметры: count - количество билетов,
    series - номер серии, необязательный аргумент length - количество цифр
    в номере, по умолчанию равен 6, выход - строка вида: <номер билета> <серия билета>
    """
             
    gener_series = gen_series(series)
    ser = next(gener_series)
    i = 0;
    while i < count :
        i +=1
        if i >= 10**length :
            i = i - (10**length-1)
            count = count- 10**length
            ser = next(gener_series)
        answer = str(i).zfill(length) + " " + ser
        yield answer
