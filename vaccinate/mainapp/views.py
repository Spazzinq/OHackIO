from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django import forms
from firebase import firebase
import bs4

db = firebase.FirebaseApplication("https://vaccinate-a2930-default-rtdb.firebaseio.com/", None)

class ProviderLogin(forms.Form):
    name = forms.CharField(label="Provider Name")
    address = forms.CharField(label="Provider Address")
    link = forms.CharField(label="link")


class AppointmentInfo(forms.Form):
    date = forms.DateField(label="Appointment Date")
    time = forms.TimeField(label="Appointment Time")
    type = forms.CharField(label="Vaccine Type")

def mainpage(request):
    return render(request,"main.html")


locationsList = [("value","name"),("value","name"),("value","name")]
class locationForm(forms.Form):
	location = forms.ChoiceField(choices = locationsList)

def providerForm(request):
    if request.method == "POST":
        form = ProviderLogin(request.POST)
        if form.is_valid():
            provider_name = form.cleaned_data['name']
            provider_address = form.cleaned_data['address']
            provider_link = form.cleaned_data['link']

            request.session['provider_name'] = provider_name
            request.session['provider_address'] = provider_address
            request.session['provider_link'] = provider_link

            return HttpResponseRedirect(reverse("providerDashboard"))

    return render(request,"formtesting.html",{"form":ProviderLogin})

def formresult(request):
    name = request.session['provider_name']
    address = request.session['provider_address']
    return render(request,"formresulttest.html", {"test":(name + " " + address)})

def providerDashboard(request):
    name = request.session['provider_name']
    address = request.session['provider_address']
    link = request.session['provider_link']

    if request.method == "POST":
        form = AppointmentInfo(request.POST)
        if form.is_valid():
            appDate = form.cleaned_data['date']
            appTime = form.cleaned_data['time']
            shotType = form.cleaned_data['type']

            DataTime = str(appDate) + " " + str(appTime)

            locations = []
            results = db.get('',None).values()

            db.put(name, address, {DataTime: {"link":link,"type": shotType}})

            return HttpResponseRedirect(reverse("submitted"))


    return render(request,"providerDashboard.html",{"providername" :name, "form":AppointmentInfo})


def submitted(request):
    return render(request,"submitted.html")

def addAddresses(request):
    with open("templates/map.html") as map:
        txt = map.read()
        txt = bs4.BeautifulSoup(txt)

    fullDb = db.get('', None).values()
    locations = []
    for name in fullDb:
        for address in name:
            locationValue = txt.new_tag("option", address, value=address)
            locations.append(locationValue)
    for location in locations:
        txt.head.append(location)

    with open("templates/map.html", "w") as map:
        map.write(str(txt))

    return render(request, "map.html")

def getData(request):
    fullDb = db.get('', None).values()
    test = []

    if request.method == "POST":
        form = locationForm(request.POST)
        if form.is_valid():
            address = form.cleaned_data['location']

            for name in fullDb:
                for addressName in name.keys():
                    if addressName == address:
                        for addressDict in name.values:
                            print(addressDict)
                            for appointment in addressDict:
                                if(appointment.find("L") == -1):
                                    test.append(appointment)


    table = ""
    for time in test:
        table = table + time + "\n"
    print(table)
    return render(request, "map.html", {"form":locationForm,"table":table})
