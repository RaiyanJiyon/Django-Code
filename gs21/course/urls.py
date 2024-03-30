from django.urls import path
from . import views

urlpatterns = [
    path('LDJ/', views.learn_django, name='courseone'),
]
