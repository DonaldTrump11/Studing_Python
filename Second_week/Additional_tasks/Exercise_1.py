def gen_number(length=6):
    """
    генератор номеров лотерейных билетов в одной серии, входные параметры:
    необязательный аргумент length - количество цифр в номере, по умолчанию равен 6
    """
    all_tickets = []
    for i in range(1, 10**length) :
        all_tickets.append(str(i).zfill(length))
    return all_tickets
    pass


def gen_series(series):
    """
    генератор серий лотерейных билетов, входные параметры: series -  - номер серии,
    выход - строка, состоящая из двух заглавных букв латинского алфавита
    """
    all_series = []
    for i in range(ord(series[0].lower()), 123) :
        for j in range(97, 123):
            all_series.append((chr(i)+chr(j)).upper())

    x = 0;
    while x <= len(all_series):
        if all_series[x] == series.upper():
            break;
        else:
            all_series.pop(x)

    return all_series
    pass


def gen_ticket_number(count, series, length=6):
    """
    генератор номеров билетов, входные параметры: count - количество билетов,
    series - номер серии, необязательный аргумент length - количество цифр
    в номере, по умолчанию равен 6, выход - строка вида: <номер билета> <серия билета>
    """
    all_tickets = []
    j = 0

    num = 0
    while num < count:
        if num >= (10 ** length):
            j = j + 1
            num = 0
            count = count - (10 ** length - 1);
        else :
            all_tickets.append([str(num+1).zfill(length), gen_series(series)[j]])
        num += 1


    return all_tickets
    pass
