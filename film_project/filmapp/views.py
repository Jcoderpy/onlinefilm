from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from filmapp.models import Film
from .forms import MovieForm


def index(request):
    movie = Film.objects.all
    context = {
        'movie_list': movie
    }
    return render(request, 'INDEX.html', context)


def detail(request, movie_id):
    movie = Film.objects.get(id=movie_id)
    return render(request, 'detail.html', {'movie': movie})


def add_movie(request):
    if request.method == 'POST':
        n = request.POST.get('name')
        f = request.POST.get('few')
        y = request.POST.get('year')
        i = request.FILES['img']
        movie = Film(n=n, f=f, y=y, i=i)
        movie.save()
        return redirect('/')

    return render(request, 'add.html')


def update(request, id):
    movie = Film.objects.get(id=id)
    form = MovieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request, 'edit.html', {'form': form, 'movie': movie})


def delete(request, id):
    if request.method == 'POST':
        movie = Film.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')
