from django.shortcuts import render
from .models import Movie

# Create your views here.
def index(request):
    reviews=Movie.objects.all()
    return render(request, 'home/list.html' , {'reviews' : reviews})