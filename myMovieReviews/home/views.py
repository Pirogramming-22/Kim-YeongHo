from django.shortcuts import render
from .models import Movie

# Create your views here.
def index(request):
    if(request.method == "POST"):
        movie = Movie.objects.create(
            title = request.POST['title'],
            releasedYear = request.POST['releasedYear'],
            genre = request.POST['genre'],
            stars = request.POST['stars'],
            runningTime = request.POST['runningtime'],
            comments = request.POST['reviewText'],
            director = request.POST['director'],
            actors = request.POST['actors'],
        )
        reviews=Movie.objects.all()
    else:
        reviews=Movie.objects.all()

    return render(request, 'home/list.html' , {'reviews' : reviews})

def add(request):
    return render(request , 'home/review.html')

def detail(request):
    return render(request , 'home/detail.html')