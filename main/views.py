from typing import Any

from django.shortcuts import render
from django.http import HttpResponse


def index(request):

    context: dict[str, str]={
        'title': 'HOUSEHOLDS - Главная',
        'content': 'Магазин товаров для дома "HOUSEHOLDS"',
    }
    return render(request,'main/index.html', context)

def about(request):
    context: dict[str, Any] = {
        'title': 'HOUSEHOLDS - О нас',
        'content': "О нас",
        'text_on_page': "Если ваша цель – купить товары для дома оптом, вы попали в нужное место. "
                "Компания 'HOUSEHOLDS' предлагает взаимовыгодное сотрудничество в сфере оптовой торговли товарами для дома. "
                "Нашими клиентами могут стать как торговые компании, так и физические лица-предприниматели."
                "Внимательное отношение к запросам клиентов, а также разумные цены, прозрачные условия и обязательность "
                "позволили нашему предприятию занять крепкое место на рынке товаров для дома  Украины."

    }
    return render(request,'main/about.html', context)


def contacts(request):
    context: dict[str, Any] = {
        'title': 'HOUSEHOLDS - Контакты',
        'content': "Контакты",
        'text_on_page': "..."
    }
    return render(request, 'main/contacts.html', context)


def delivery(request):
    context: dict[str, Any] = {
        'title': 'HOUSEHOLDS - Доставка и отпата',
        'content': "Доставка и отпата",
        'text_on_page': "..."
    }
    return render(request, 'main/delivery.html', context)