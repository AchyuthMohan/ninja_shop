

from django.contrib import admin
from django.urls import path
from django.urls.conf import include
import main
from main import urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(main.urls)),
    path('register/',include(main.urls)),
]
