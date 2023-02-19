from django.contrib import admin
from django.urls import path, include
from core.urls import router
from core.apiViews import Logout


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('logout', Logout.as_view())
]
