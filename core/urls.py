from rest_framework import routers
from core.apiViews import PaperViewSet


router = routers.DefaultRouter()
router.register('papeis/', PaperViewSet, basename='Paper')
