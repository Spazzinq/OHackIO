from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django import forms


class ProviderLogin(forms.Form):
    name = forms.CharField(label="Provider Name")
    address = forms.CharField(label="Provider Address")


class AppointmentInfo(forms.Form):
    date = forms.DateField(label="Appointment Date")
    time = forms.TimeField(label="Appointment Time")
    type = forms.CharField(label="Vaccine Type")


def providerForm(request):
    if request.method == "POST":
        form = ProviderLogin(request.POST)
        if form.is_valid():
            provider_name = form.cleaned_data['name']
            provider_address = form.cleaned_data['address']

            request.session['provider_name'] = provider_name
            request.session['provider_address'] = provider_address

            return HttpResponseRedirect(reverse("providerDashboard"))

    return render(request,"formtesting.html",{"form":ProviderLogin})

def formresult(request):
    name = request.session['provider_name']
    address = request.session['provider_address']
    return render(request,"formresulttest.html", {"test":(name + " " + address)})

def providerDashboard(request):
    name = request.session['provider_name']
    address = request.session['provider_address']

    if request.method == "POST":
        form = AppointmentInfo(request.POST)
        if form.is_valid():
            appDate = form.cleaned_data['date']
            appTime = form.cleaned_data['time']
            appType = form.cleaned_data['type']

            DataTime = str(appDate) + " " + str(appTime)
            #put this data into database
            return HttpResponseRedirect(reverse("submitted"))


    return render(request,"providerDashboard.html",{"providername" :name, "form":AppointmentInfo})


def submitted(request):
    return render(request,"submitted.html")
