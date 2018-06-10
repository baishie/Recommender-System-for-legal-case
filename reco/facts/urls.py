
from django.urls import path
from facts.views import IndexView
from django.conf.urls import url

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
