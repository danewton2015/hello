# Create your views here.
from django.shortcuts import render


def hello(request):
    context={}
    return render(request, 'one.html', context)
