from django.http import HttpResponse
from django.shortcuts import render,redirect, get_object_or_404
from . models import Category,Movie
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from django.contrib.auth.models import User,auth
from django.contrib import messages,auth
from django.urls import reverse
from . forms import Movieform


# Create your views here.
def allMovieCat(request,c_slug=None):
    c_page=None
    movies_list=None
    if c_slug!=None:
        c_page=get_object_or_404(Category,slug=c_slug)
        movies_list=Movie.objects.all().filter(category=c_page)

    else:
       movies_list=Movie.objects.all().filter()
    paginator=Paginator(movies_list,6)
    try:
        page=int(request.GET.get('page',1))
    except:
        page=1
    try:
        movies=paginator.page(page)
    except (EmptyPage,InvalidPage):
        movies=paginator.page(paginator.num_pages)

    return render(request,"category.html",{'category':c_page,'movies':movies})

def movieDetail(request,c_slug,movie_slug):
    try:
        movie=Movie.objects.get(category__slug=c_slug,slug=movie_slug)
    except Exception as e:
        raise e
    return render(request,'product.html',{'movie':movie})

def addmovie(request):
    forms=Movieform()
    if request.method == 'POST':
        forms = Movieform(request.POST)
        name = request.POST.get('name')
        description = request.POST.get('description')
        date = request.POST.get('date')
        image = request.FILES['image']
        category = request.POST.get('category')
        actors = request.POST.get('actors')
        youtube = request.POST.get('youtube')
        movie = Movieform(name=name, description=description, date=date, image=image, category=category,
                              actors=actors, youtube=youtube)
        movie.save()
        return redirect('moviesapp:allMovieCat')

    return render(request, 'addmovie.html')

