from django.shortcuts import render
from django.shortcuts import redirect
from MainPage.models import Doctor, Review, BadWords, ExceptionWords
from django.http import Http404
import datetime


def add_review(request, ide):
    """

    процедура добавления отзыва о докторе с заданным id
    """
    doc = Doctor.objects.get(id=ide)
    specials = list(Doctor.objects.get(id=ide).specialities.all().values("specialty"))
    if request.method == "POST":
        re = request.POST['comment']
        if len(re) < 100:
            return redirect('error/')
        # сохранение отзыва, если его длина более 100
        review = Review.objects.create(
            doctor=doc,
            dt_created=datetime.datetime.now(),
            dt_updated=datetime.datetime.now(),
            first_review=re,
            changed_review=re,
            ip_address=request.META['REMOTE_ADDR'],
            user=request.user
            )
        review.save()
        return redirect('verification/')
    context = {'doc': doc, 'specials': specials}
    return render(request, 'form.html', context)


def verification(request, ide):
    """

    подтверждение отправки отзыва
    """
    return render(request, 'verification.html')


def error(request, ide):
    """

    сообщение об ошибке
    """
    return render(request, 'Error.html')


def show_review(request):
    """
    выводит список отзывов
    """
    if not request.user.is_staff:
        raise Http404

    reviews = Review.objects.all().order_by("dt_created").select_related('doctor').prefetch_related('doctor__specialities')
    # список матерных слов и исключений получим отдельно
    bad_ws = BadWords.objects.values_list("bad_word", flat=True)
    ex_ws = ExceptionWords.objects.values_list("exception_word", flat=True)
    # но передадим у шаблон как единый аргумент словаря
    all_ws = {'bad_words': bad_ws, 'exception_words':  ex_ws}
    return render(request, 'Review.html', {
        'reviews': reviews,
        'all_words': all_ws,

    })


def welcome(request):
    """

    стартовая страница
    """
    err = ''
    if request.method == "POST":
        doctor_id = str(request.POST['doctor_id']).strip()
        if doctor_id.isdigit():
            return redirect('add-review/' + doctor_id)
        err = 'Вы ввели некорректные данные, id доктора должен быть числом!'
    return render(request, 'welcome.html', {'error': err})

