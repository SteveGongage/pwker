from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
import datetime

# Create your views here.

def mainPage(request):
    return render(request, 'mainPage.html', {
    })


def regions(request):
    return render(request, 'regions.html', {
    })
