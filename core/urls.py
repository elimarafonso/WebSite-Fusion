from django.urls import path
from unicodedata import name

from core.views import IndexView, Formulario


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('teste/', Formulario.as_view(), name='teste'),
]


