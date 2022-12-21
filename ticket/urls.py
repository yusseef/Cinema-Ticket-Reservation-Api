from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
router = DefaultRouter()
router.register('', Reservation)

urlpatterns = [
    path('movies/', movielist, name = 'moviesList'),
    path('movies/<str:pk>/', movie_pk, name = 'moviesPK'),
    path('halls/', ListHalls.as_view(), name = 'listHalls'),
    path('halls/<str:pk>/', HallPk.as_view(), name = 'hallPK'),
    path('guests/', GuestList.as_view(), name = 'listGuests'),
    path('guests/<str:pk>/', GuestPk.as_view(), name = 'GuestPK'),
    path('reservations/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),



    
]