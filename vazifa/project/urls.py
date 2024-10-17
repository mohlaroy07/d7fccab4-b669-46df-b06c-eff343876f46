from django.urls import path
from . import views

urlpatterns = [
    path("", views.city_list, name="city_list"),
    path("city/<int:pk>/", views.city_detail, name="city_detail"),
]
