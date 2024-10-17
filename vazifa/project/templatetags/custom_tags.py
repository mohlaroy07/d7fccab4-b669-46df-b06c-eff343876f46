from django import template

register = template.Library()

from project.models import City, Hotel


@register.simple_tag
def city_count():
    return City.objects.count()


@register.simple_tag
def hotel_count(city_id: int):
    return Hotel.objects.filter(city_id=city_id).count()
