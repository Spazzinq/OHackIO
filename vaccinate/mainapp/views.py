from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django import forms


class ProviderLogin(forms.Form):
    name = forms.CharField(label="Provider Name")
    address = forms.CharField(label="Provider Address")


def providerForm(request):
    if request.method == "POST":
        form = ProviderLogin(request.POST)
        if form.is_valid():
            provider_name = form.cleaned_data['name']
            provider_address = form.cleaned_data['address']

            request.session['provider_name'] = provider_name
            request.session['provider_address'] = provider_address

            return HttpResponseRedirect(reverse("formresult"))

    return render(request,"formtesting.html",{"form":ProviderLogin})

def formresult(request):
    name = request.session['provider_name']
    address = request.session['provider_address']
    return render(request,"formresulttest.html", {"test":(name + " " + address)})
