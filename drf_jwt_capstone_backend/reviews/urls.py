from django.urls import path
from . import views

urlpattern = [
    path('', views.ReviewsList.as_view()),
    path('<int:pk>/', views.ReviewDetail.as_view()),
]