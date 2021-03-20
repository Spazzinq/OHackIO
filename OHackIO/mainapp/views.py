from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django import forms


class ProviderLogin(forms.Form):
    name = forms.CharField(label="Provider Name")
    address = forms.CharField(label="Provider Address")


def providerForm(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            provider_name = form.cleaned_data['name']
            provider_address = form.cleaned_data['address']
            return HttpResoibsedRedurst(reverse("formresult"))

    return render(request,"formtesting.html",{"form":ProviderLogin})

def formresult(request):
    return render(request,"formresulttest.html", {"test":(provider_name + " " + provider_address)})
