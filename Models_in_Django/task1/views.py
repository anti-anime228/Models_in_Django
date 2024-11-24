from django.shortcuts import render
from django.views.generic import TemplateView

from django.http import HttpResponse

from .forms import UserRegister
from .models import Buyer, Game


def views1(request):
    return render(request, 'func_template.html')


class views2(TemplateView):
    template_name = 'class_template.html'


def main_page(request):
    name = 'Все игры.ру'

    context = {
        'name': name
    }
    return render(request, 'main_page.html', context)










def shop_page(request):
    name = 'Магазин'
    games = Game.objects.all()
    # games = Game.objects.all().values()

    context = {'games': games, 'name': name}

    return render(request, 'shop.html', context)









































def basket_page(request):
    return render(request, 'basket.html')


def sign_up_by_html(request):
    all_names = Buyer.objects.values_list('name', flat=True)
    users = [str(i).lower() for i in all_names]
    info = {}

    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if password == repeat_password and int(age) > 18 and username not in users:
            new_buyer = Buyer.objects.create(name=username, balance=0, age=age)
            return HttpResponse(f'Приветствуем, {username}')
        else:
            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif int(age) <= 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in users:
                info['error'] = 'Пользователь уже существует'

    return render(request, 'registration_page.html', context=info)


def sign_up_by_django(request):
    all_names = Buyer.objects.values_list('name', flat=True)
    users = [str(i).lower() for i in all_names]
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username'].lower()
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if password == repeat_password and int(age) > 18 and username not in users:
                return HttpResponse(f'Приветствуем, {username}')
            else:
                if password != repeat_password:
                    info['error'] = 'Пароли не совпадают'
                elif int(age) <= 18:
                    info['error'] = 'Вы должны быть старше 18'
                elif username in users:
                    info['error'] = 'Пользователь уже существует'

    return render(request, 'registration_page.html', context=info)
