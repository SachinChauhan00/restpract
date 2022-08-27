from cgitb import lookup
from unittest.mock import MagicProxy
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView
from restcrud.serializers import *
from rest_framework import viewsets
from restcrud.models import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.exceptions import ValidationError
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated



class SongsViewset(viewsets.ModelViewSet):
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ArtistViewset(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

class AlbumViewset(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
# class SongsList(ListAPIView):
#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     permission_classes = [IsAuthenticated]
#     queryset = Songs.objects.all()
#     serializer_class = SongsSerializer
#     filter_backends = [DjangoFilterBackend,SearchFilter]
#     filterset_fields = ['id','album']
#     search_fields = ['song_name']
    
# class SongsCreate(CreateAPIView):
#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     permission_classes = [IsAuthenticated]
#     queryset = Songs.objects.all()
#     serializer_class = SongsSerializer

# class SongsDelete(DestroyAPIView):
#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     permission_classes = [IsAuthenticated]
#     queryset = Songs.objects.all()
#     serializer_class = SongsSerializer
#     lookup_field = 'id'
    
# class SongsUpdate(UpdateAPIView):
#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     permission_classes = [IsAuthenticated]
#     queryset = Songs.objects.all()
#     serializer_class = SongsSerializer
#     lookup_field = 'id'
    
# class AlbumList(ListAPIView):
#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     permission_classes = [IsAuthenticated]
#     queryset = Album.objects.all()
#     serializer_class = AlbumSerializer

# class AlbumCreate(CreateAPIView):
#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     permission_classes = [IsAuthenticated]
#     queryset = Album.objects.all()
#     serializer_class = AlbumSerializer

# class AlbumDelete(DestroyAPIView):
#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     permission_classes = [IsAuthenticated]
#     queryset = Album.objects.all()
#     serializer_class = AlbumSerializer
#     lookup_field = 'id'
    
# class AlbumUpdate(UpdateAPIView):
#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     permission_classes = [IsAuthenticated]
#     queryset = Album.objects.all()
#     serializer_class = AlbumSerializer
#     lookup_field = 'id'
    
# class ArtistList(ListAPIView):
#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     permission_classes = [IsAuthenticated]
#     queryset = Artist.objects.all()
#     serializer_class = ArtistSerializer
    
# class ArtistCreate(CreateAPIView):
#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     permission_classes = [IsAuthenticated]
#     queryset = Artist.objects.all()
#     serializer_class = ArtistSerializer

# class ArtistDelete(DestroyAPIView):
#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     permission_classes = [IsAuthenticated]
#     queryset = Artist.objects.all()
#     serializer_class = ArtistSerializer
#     lookup_field = 'id'
    
# class ArtistUpdate(UpdateAPIView):
#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     permission_classes = [IsAuthenticated]
#     queryset = Artist.objects.all()
#     serializer_class = ArtistSerializer
#     lookup_field = 'id'
