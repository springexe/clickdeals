from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost
# Create your views here.
def index(request):
    return render(request ,'blog/index.html')

def blogpost(request, id):
    post = Blogpost.objects.filter(post_id = id)[0]
    # params = {'allblog':allblog}
    print(post)
    params={'post':post}
    return render(request ,'blog/blogpost.html',params)