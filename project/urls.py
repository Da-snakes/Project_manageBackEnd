from django.urls import path

from . import views

urlpatterns = [
    path('p/',views.person),
    path('tache/', views.tache),
    path('login/', views.login),
]
