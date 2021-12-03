from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView
from ..locations.views import LocationList, LocationDetail
from ..replies.views import RepliesList, ReplyDetail
from ..reviews.views import ReviewsList, ReviewDetail
from ..trips.views import TripsList, TripDetail

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('locations/', LocationList.as_view(), name='locations'),
    path('locations/<int:pk>/', LocationDetail.as_view(), name='location_detail'),
    path('replies/', RepliesList.as_view(), name='replies'),
    path('replies/<int:pk>/', ReplyDetail.as_view(), name='reply_detail'),
    path('reviews/', ReviewsList.as_view(), name='reviews'),
    path('reviews/<int:pk>/', ReviewDetail.as_view(), name='review_detail'),
    path('trips/', TripsList.as_view(), name='trips'),
    path('trips/<int:pk>/', TripDetail.as_view(), name='trip_detail'),
]
