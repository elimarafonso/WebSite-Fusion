from django.urls import path
from unicodedata import name

from core.views import IndexView, TestemunhoView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('testemunho/', TestemunhoView.as_view(), name='testemunho'),
]


