from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('', Reservation)

urlpatterns = [
    path('movies/', movielist, name = 'moviesList'),
    path('movies/<str:pk>/', movie_pk, name = 'moviesPK'),
    path('halls/', ListHalls.as_view(), name = 'listHalls'),
    path('halls/<str:pk>/', HallPk.as_view(), name = 'hallPK'),
    path('guests/', GuestList.as_view(), name = 'listGuests'),
    path('guests/<str:pk>/', GuestPk.as_view(), name = 'GuestPK'),
    path('reservations/', include(router.urls))



    
]