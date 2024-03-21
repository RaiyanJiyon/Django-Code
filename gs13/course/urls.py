from django.urls import path
from . import views

urlpatterns = [
    path('learndj/', views.learn_django),
    path('floatdj/', views.float_format),
    path('tagsdj/', views.django_tag),
    path('exmp2/', views.example_two),
    path('exmp3/', views.example_three),
    path('exmp4/', views.example_four),
    path('exmp5/', views.example_five),
]
