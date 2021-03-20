from django.urls import path
from . import views

urlpatterns = [
    path('',views.getData, name="getData"),
    path('map.html',views.getData, name="map.html")
]
