from django.db import models
from django.contrib.auth.models import User
import MainPage.text_change as text_change


class Specialty(models.Model):
    # специальноси врачей
    specialty = models.CharField(max_length=100, verbose_name='Специальность:')

    class Meta:
        verbose_name = 'Специальность'
        verbose_name_plural = 'Специальности'

    def __str__(self):
        return self.specialty


class Doctor(models.Model):
    # информация о врачах
    name = models.CharField(max_length=100, verbose_name='Имя')
    surname = models.CharField(max_length=100, verbose_name='Фамилия')
    fathername = models.CharField(max_length=100, verbose_name='Отчество', blank=True)
    specialities = models.ManyToManyField(Specialty, verbose_name='Специальности', blank=True)

    class Meta:
        verbose_name = 'Врач'
        verbose_name_plural = 'Врачи'

    def __str__(self):
        return "%s %s %s" % (self.name, self.surname, self.fathername)


class Review(models.Model):
    # отзывы
    doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT, verbose_name='Врач')
    dt_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    dt_updated = models.DateTimeField(auto_now=True, verbose_name='Дата и время последнего изменения')
    first_review = models.TextField(verbose_name='Исходный отзыв')
    changed_review = models.TextField(verbose_name='Изменённый отзыв')
    ip_address = models.GenericIPAddressField(verbose_name='IP-адрес')
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Имя пользователя', blank=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return "%s %s %s" % (self.user, str(self.dt_created), self.doctor)

    def save(self, *args, **kwargs):
        # преобразование текста, влияющее на регистр, повторяющиеся знаки препинания и т.д.
        self.changed_review = text_change.text_change(self.first_review)
        super(Review, self).save(*args, **kwargs)


class BadWords(models.Model):
    # справочник матерных слов
    bad_word = models.CharField(max_length=200, verbose_name='Матерное слово')

    class Meta:
        verbose_name = 'Матерное слово'
        verbose_name_plural = 'Матерные слова'

    def __str__(self):
        return str(self.bad_word)


class ExceptionWords(models.Model):
    # список исключений
    exception_word = models.CharField(max_length=200, verbose_name='Слова-исключения')

    class Meta:
        verbose_name = 'Слово-исключение'
        verbose_name_plural = 'Слова-исключения'

    def __str__(self):
        return str(self.exception_word)








