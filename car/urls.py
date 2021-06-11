from django.urls import path, include
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
]
