from django.urls import path
from . import views

urlpatterns = [
    path('', views.LocationList.as_view()),
    path('<int:pk>/', views.LocationDetail.as_view()),
]