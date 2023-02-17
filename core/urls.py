from rest_framework import routers
from core.apiViews import PaperViewSet, UserViewSet, WalletViewSet


router = routers.DefaultRouter()
router.register('papeis', PaperViewSet, basename='Paper')
router.register('usuarios', UserViewSet, basename='User')
router.register('carteira',WalletViewSet, basename='Wallet')
