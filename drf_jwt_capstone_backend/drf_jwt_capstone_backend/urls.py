"""drf_jwt_capstone_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from locations.views import LocationList, LocationDetail
from replies.views import RepliesList, ReplyDetail
from reviews.views import ReviewsList, ReviewDetail
from trips.views import TripsList, TripDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('authentication.urls')),
    path('locations/', LocationList.as_view(), name='locations'),
    path('locations/<int:pk>/', LocationDetail.as_view(), name='location_detail'),
    path('replies/', RepliesList.as_view(), name='replies'),
    path('replies/<int:pk>/', ReplyDetail.as_view(), name='reply_detail'),
    path('reviews/', ReviewsList.as_view(), name='reviews'),
    path('reviews/<int:pk>/', ReviewDetail.as_view(), name='review_detail'),
    path('trips/', TripsList.as_view(), name='trips'),
    path('trips/<int:pk>/', TripDetail.as_view(), name='trip_detail'),
]
