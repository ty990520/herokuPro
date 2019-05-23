from django.contrib import admin
from django.urls import path
import hero.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hero.views.home, name="home"),
]
