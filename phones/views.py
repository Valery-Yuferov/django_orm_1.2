
from django.shortcuts import render, redirect

from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    sort = request.GET.get('sort')

    if sort == 'name':
        phones = phones.order_by('name')
    elif sort == 'min_price':
        phones = phones.order_by('price')
    elif sort == 'max_price':
        phones = phones.order_by('-price')

    context = {'phones': phones}
    print(context, template)
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    print(context, template)
    return render(request, template, context)


# import json
# from django.http import JsonResponse
#
# def show_catalog(request):
#     phones = Phone.objects.all()
#     phone_data = [{'name': phone.name, 'price': phone.price} for phone in phones]
#
#     return JsonResponse({'phones': phone_data})


