from rest_framework import routers
from core.apiViews import PaperViewSet, UserViewSet


router = routers.DefaultRouter()
router.register('papeis', PaperViewSet, basename='Paper')
router.register('usuarios', UserViewSet, basename='User')
