from django.urls import path

from peters.events import views

urlpatterns = [
    path('', views.index, name='index'),
]