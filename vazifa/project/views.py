from django.shortcuts import render
from .models import City, Hotel


def city_list(request):
    cities = City.objects.all()
    return render(request, "index.html", {"cities": cities})


def city_detail(request, pk: int):
    city = City.objects.get(pk=pk)
    return render(request, "detail.html", {"city": city})
