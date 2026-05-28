from django.urls import path
from . import views

urlpatterns = [

    path("", views.home, name="home"),

    path("berita/", views.berita, name="berita"),

]