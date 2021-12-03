from django.urls import path
from . import views

urlpattern = [
    path('', views.TripsList.as_view()),
    path('<int:pk>/', views.TripDetail.as_view()),
]