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


locationsList = [("value","name"),("value","name"),("value","name")]
class locationForm(forms.Form):
	location = forms.ChoiceField(choices = locationsList)

def providerForm(request):
    if request.method == "POST":
        form = ProviderLogin(request.POST)
        if form.is_valid():
            provider_name = form.cleaned_data['name']
            provider_address = form.cleaned_data['address']
            return HttpResponseRedirect(reverse("formresult"))

    return render(request,"formtesting.html",{"form":ProviderLogin})

def formresult(request):
    return render(request,"formresulttest.html", {"test":(provider_name + " " + provider_address)})

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
    return render(request, "map.html", {"form":locationForm,"table":table)
