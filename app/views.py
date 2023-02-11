from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def omlet (request):
    sostav = {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    }
    kol = int(request.GET.get("servings",1))
    list_ingrid = []
    list_kol =[]

    for key, value  in sostav.items():
        list_ingrid.append(key)
        list_kol.append(float(value)*kol)

    new_sostav = list(zip(list_ingrid,list_kol))

    context = {
        'recept': new_sostav
        }
    return render(request, 'recept.html', context)


def pasta(request):
    sostav = {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    }
    kol = int(request.GET.get("servings",1))
    list_ingrid = []
    list_kol = []

    for key, value in sostav.items():
        list_ingrid.append(key)
        list_kol.append(float(value) * kol)

    new_sostav = list(zip(list_ingrid, list_kol))

    context = {
        'recept': new_sostav
    }
    return render(request, 'recept.html', context)




