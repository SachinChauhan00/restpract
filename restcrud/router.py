from .api_views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('songs',SongsViewset)
router.register('albums',AlbumViewset)
router.register('artists',ArtistViewset)
