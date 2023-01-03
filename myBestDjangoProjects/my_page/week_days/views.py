from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

people = [
    'Жукова Анна Константиновна',
    'Юлия Степановна Потапова',
    'Гущин Аполлинарий Тимурович',
    'Дорофей Ярославович Третьяков',
    'Селезнева Анна Тарасовна',
    'Федотов Симон Харлампьевич',
    'Красильникова Вера Борисовна',
    'Бажен Тихонович Костин',
    'Веселова Анжелика Тимофеевна',
    'Щербаков Самсон Феодосьевич'
]

people1 = [
    {'name': 'Жанна Ивановна Бобылева', 'age': 28, 'phone': '+72609577301'},
    {'name': 'Спиридон Феликсович Алексеев', 'age': 48, 'phone': '8 445 133 42 50'},
    {'name': 'Лыткина Зоя Рубеновна', 'age': 34, 'phone': '84061070300'},
    {'name': 'Олимпиада Святославовна Петухова', 'age': 70, 'phone': '8 740 992 96 95'},
    {'name': 'Лазарева Нина Кирилловна', 'age': 67, 'phone': '89040731989'},
    {'name': 'Каллистрат Ильич Ширяев', 'age': 63, 'phone': '+7 418 298 8976'},
    {'name': 'Евсеев Любосмысл Чеславович', 'age': 47, 'phone': '83111461302'},
    {'name': 'Прохор Харламович Артемьев', 'age': 47, 'phone': '+77827445919'},
    {'name': 'Кондрат Игнатьевич Ершов', 'age': 35, 'phone': '+7 419 594 39 00'},
    {'name': 'Ипат Власович Ильин', 'age': 47, 'phone': '88004779773'}
]

dict_days = {
    'mondey': 'список дел, запланированных на понедельник',
    'tuesday': 'список дел, запланированных на вторник',
    'Wednesday': 'список дел, запланированных на среду',
    'Thursday': 'список дел, запланированных на четверг',
    'Friday': 'список дел, запланированных на пятницу',
    'Saturday ': 'список дел, запланированных на субботу',
    'Sunday': 'список дел, запланированных на воскересние',
}

# Create your views here.


# def monday(request):
#     return HttpResponse(' список дел, запланированных на понедельник')


def the_chousen_day(request, day):
    the_day = dict_days.get(day)
    if the_day:
        return HttpResponse(the_day)
    else:
        return HttpResponseNotFound(f'такого дня в списке нет {day}')


def the_chousen_day_by_number(request, day: int):
    return render(request, 'week_days/greeting.html')
# def tuesday(request):
#     return HttpResponse(' список дел, запланированных на вторник')


# def get_info_about_people(request):
#     return render(request, 'week_days/people.html', context={'people': people})


def get_info_about_people(request):
    return render(request, 'week_days/people1.html', context={'people': people1})