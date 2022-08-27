"""restpract URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from restcrud import api_views
from restcrud import views
from restcrud.router import *

urlpatterns = [
    # songs
    # path('songs/',api_views.SongsList.as_view(),name='songs'),
    # path('songs/create',api_views.SongsCreate.as_view(),name='songs'),
    # path('songs/update/<int:id>',api_views.SongsUpdate.as_view(),name='songsup'),
    # path('songs/delete/<int:id>',api_views.SongsDelete.as_view(),name='songsdel'),
    # # album
    # path('album/',api_views.AlbumList.as_view(),name='album'),
    # path('album/create',api_views.AlbumCreate.as_view(),name='album'),
    # path('album/update/<int:id>',api_views.AlbumUpdate.as_view(),name='albumup'),
    # path('album/delete/<int:id>',api_views.AlbumDelete.as_view(),name='albumdel'),
    # # artist
    # path('artist/',api_views.ArtistList.as_view(),name='artist'),
    # path('artist/create',api_views.ArtistCreate.as_view(),name='artist'),
    # path('artist/update/<int:id>',api_views.ArtistUpdate.as_view(),name='artistup'),
    # path('artist/delete/<int:id>',api_views.ArtistDelete.as_view(),name='artistdel'),
    path('api/',include(router.urls)),
    path('admin/', admin.site.urls),
    # path('',views.index,name='index')
]
