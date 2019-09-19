from django import template

register = template.Library()


def red(s, all_words):
    # разделим all_words на мат и исключения
    bad_words = all_words['bad_words']
    exception_words = all_words['exception_words']
    lst1 = [i for i in s.split()]
    s1 = ''
    f = False
    for word in lst1:
        for i in bad_words:
            if word == i:  # если слово совпадает с матом
                f = True
                s1 += '<span style="color:red">' + word + '</span>' + ' '
            elif (word[:len(i)] == i) and (word not in exception_words):  # если слово начинается с мата
                f = True
                s1 += '<span style="color:red">' + i + '</span>' + word[len(i)+1:] + ' '
            elif (word[-len(i):] == i) and (word not in exception_words):  # если слово оканчивается матом
                f = True
                s1 += word[:-len(i)-1] + '<span style="color:red">' + i + '</span>' + ' '
        if not f:
            s1 += word + ' '
    return s1


register.filter('red', red)

