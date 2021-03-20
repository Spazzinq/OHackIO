from django.urls import path
from . import views

urlpatterns = [
    path('',views.providerForm,name="providerForm")
]
