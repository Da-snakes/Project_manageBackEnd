from django.urls import include, path

from . import views


urlpatterns = [
    path('persons/', views.PersonAPIView.as_view()),
    path('tasks/', views.TaskAPIView.as_view()),
    path('portfolios/', views.PortfolioAPIView.as_view()),
    path('widgets/', views.WidgetAPIView.as_view()),
    path('positions/', views.PositionAPIView.as_view()),

]