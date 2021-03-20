from django.urls import path
from . import views

urlpatterns = [
    path('providerForm/',views.providerForm, name="providerForm"),
    path('map/',views.getData, name="getData")
]
