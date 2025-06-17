
from django.http import HttpResponse
from django.shortcuts import render
from.models import todoliste,item

def index (response,name):
    ls=todoliste.objects.get(name=name)
    item=ls.item_set.get(id=1)
    return HttpResponse("<h1>%s</h1><br><p>%s</p>"%(ls.name,item.text))

