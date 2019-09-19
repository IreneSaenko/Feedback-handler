from django.contrib import admin
from MainPage.models import *


class SpecialtyAdmin(admin.ModelAdmin):
    # таблица специальностей
    list_display = ('id', 'specialty')
    search_fields = ('specialty',)


admin.site.register(Specialty, SpecialtyAdmin)


class DoctorAdmin(admin.ModelAdmin):
    # таблица врачей
    list_display = ('id', 'name', 'surname', 'fathername')
    search_fields = ('name', 'surname')


admin.site.register(Doctor, DoctorAdmin)


class ReviewAdmin(admin.ModelAdmin):
    # таблица отзывов
    list_display = ('id', 'user', 'doctor', 'dt_created',  'dt_updated', 'first_review', 'changed_review', 'ip_address')
    readonly_fields = ('dt_created', 'first_review')
    # слишком много докторов, поэтому поле доктор мы не делаем выпадающим списком
    raw_id_fields = ('doctor',)
    search_fields = ('user', 'doctor')


admin.site.register(Review, ReviewAdmin)


class BadWordsAdmin(admin.ModelAdmin):
    # таблица матерных слов
    list_display = ('id', 'bad_word')


admin.site.register(BadWords, BadWordsAdmin)


class ExceptionWordsAdmin(admin.ModelAdmin):
    # таблица исключений
    list_display = ('id', 'exception_word',)


admin.site.register(ExceptionWords, ExceptionWordsAdmin)

