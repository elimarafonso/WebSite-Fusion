from django.urls import path
from unicodedata import name

from core.views import IndexView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]


