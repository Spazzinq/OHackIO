from django.urls import path
from . import views

urlpatterns = [
    path('',views.providerForm,name="providerForm"),
    path('formresponse/',views.formresult,name="formresult"),
    path('providerDashboard/',views.providerDashboard,name="providerDashboard"),
    path('submitted/',views.submitted,name="submitted")
]
