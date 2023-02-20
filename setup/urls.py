from django.contrib import admin
from django.urls import path, include
from core.urls import router
from rest_framework.authtoken.views import ObtainAuthToken
from core.apiViews import Logout, UsersPositionView, CalculatorView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('api-token-auth/', ObtainAuthToken.as_view()),
    path('logout', Logout.as_view(), name='logout'),
    path('posicao', UsersPositionView.as_view(), name='posicao'),
    path('calculator', CalculatorView.as_view(), name='calculator'),
]
