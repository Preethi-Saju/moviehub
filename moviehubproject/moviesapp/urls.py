from django.urls import path, include
from . import views
app_name='moviesapp'

urlpatterns = [

    path('',views.allMovieCat,name='allMovieCat'),
    path('home/<slug:c_slug>/',views.allMovieCat,name='movies_by_category'),
    path('<slug:c_slug>/<slug:movie_slug>/',views.movieDetail,name='movieCatDetail'),
    path('addmovie',views.addmovie,name='addmovie'),
]
