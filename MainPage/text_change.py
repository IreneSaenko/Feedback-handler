def text_change(s1):
    s1 = s1.strip()  # удаление пробелов в начале и конце
    s2 = ''
    signs = ['!', '?', '.', ',', ':', ';', '-']
    count = 0  # количество подряд идущих больших букв
    max_count = 0  # максимальное количество подряд идущих больших букв
    for i in range(len(s1) - 1):
        if s1[i] in signs:
            # если текущий символ знак препинания
            if s1[i] != s1[i + 1]:
                # если дальше идёт такой же зак препинания, не включаем
                if (s1[i + 1] != ' ') and (s1[i + 1] not in signs):
                    # если дальше нет пробела или другого знака препинания, то нужен пробел
                    s2 += s1[i] + ' '
                else:
                    s2 += s1[i]
        elif s1[i] == ' ':
            # если это пробел
            if (s1[i + 1] != ' ') and (s1[i + 1] not in signs):
                # и это не подряд идущие пробелы и не пробелы перед знаком препинания
                s2 += s1[i]
        else:
            # если это всё же буква
            if s1[i].isupper() and s1[i + 1].isupper():
                # подряд идущие заглавные буквы
                count += 1
            else:
                if count >= max_count:
                    max_count = count
                count = 0
            s2 += s1[i]
    # возможно в строке только заглавные буквы, тогда условие else не выполнится ни разу, max_count
    # нужно проверить ещё раз
    if count >= max_count:
        max_count = count
    s2 += s1[-1]  # последний символ в строке точно не пробел, поэтому мы его добавляем
    # на данном этапе есть строка, в которой нет повторяющихся знаков препинания и пробелов
    if max_count >= 5:
        # если есть 6 подряд идущих заглавных букв, то сделаем заглавные только в начале предложения
        s1 = s2.lower()
        s2 = s2[0].upper() + s1[1]
        for i in range(2, len(s1)):
            if s1[i - 2] in ['!', '?', '.']:
                s2 += s1[i].upper()
            else:
                s2 += s1[i]
    return s2
