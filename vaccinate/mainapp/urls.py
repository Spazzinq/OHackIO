from django.urls import path
from . import views

urlpatterns = [
    path('',views.providerForm,name="providerForm"),
    path('formresponse/',views.formresult,name="formresult")
]
