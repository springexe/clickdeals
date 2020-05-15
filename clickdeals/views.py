from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


from math import ceil
def index(request):
    return render(request,'index.html')