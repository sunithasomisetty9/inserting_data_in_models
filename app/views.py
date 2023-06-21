from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.

def insert_topic(request):
    tn=input('enter a topic name: ')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse("Topic data is created")

def insert_webpage(request):
    tn=input('enter a topic name: ')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    ne=input('enter a name: ')
    ul=input('enter url: ')
    WO=Webpage.objects.get_or_create(topic_name=TO,name=ne,url=ul)[0]
    WO.save()
    return HttpResponse("Webpage data is inserted")

def insert_accessrecord(request):
    tn=input('enter a topic name: ')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    ne=input('enter a name: ')
    ul=input('enter url: ')
    WO=Webpage.objects.get_or_create(topic_name=TO,name=ne,url=ul)[0]
    WO.save()

    d=input("enter date: ")
    a=input("enter an author: ")
    AO=AccessRecord.objects.get_or_create(name=WO,date=d,author=a)[0]
    AO.save()
    return HttpResponse("Access record data is inserted")


