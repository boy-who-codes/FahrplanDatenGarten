from django.urls import path
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView

from . import views

app_name = 'verspaeti'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
