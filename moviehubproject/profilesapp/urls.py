from django.urls import path, include
from . import views


app_name='profilesapp'

urlpatterns = [
    path('',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('logout',views.logout,name='logout'),
    path('profile',views.profile,name='profile'),



    ]