from django.shortcuts import render , redirect
from .models import Movie
from django.http import HttpResponseRedirect

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
            posterURL = request.POST['URLS'],
        )
        reviews=Movie.objects.all()
    else:
        reviews=Movie.objects.all()

    return render(request, 'home/list.html' , {'reviews' : reviews})

def add(request):
    return render(request , 'home/review.html')

def detail(request, pk):
    if(request.method == "POST"):
        movie = Movie.objects.get(id = pk)
        movie.title = request.POST['title']
        movie.releasedYear = request.POST['releasedYear']
        movie.genre = request.POST['genre']
        movie.stars = request.POST['stars']
        movie.runningTime = request.POST['runningtime']
        movie.comments = request.POST['reviewText']
        movie.director = request.POST['director']
        movie.actors = request.POST['actors']
        movie.posterURL = request.POST['URLS']
        movie.save()
    else: 
        movie = Movie.objects.get(id = pk)    
    return render(request , 'home/detail.html' , {'movie' : movie})

def delete(request , pk):
    if(request.method == 'POST'):
        movie = Movie.objects.get(id=pk)
        movie.delete()
        return redirect('home:index')
    return redirect('home:index')

def edit(request , pk):
    if(request.method == 'POST'):
        movie = Movie.objects.get(id=pk)
        return render(request , 'home/edit.html' , {'movie':movie})
    return HttpResponseRedirect(request.path)