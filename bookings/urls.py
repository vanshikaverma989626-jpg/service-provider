from django.urls import path
from . import views

urlpatterns = [
    path('book/<int:provider_id>/',views.create_booking,name='create_booking'), #<int:provider_id> - dynamic url, will be replaced by actual provider id when user clicks on book button
    path('my-bookings/',views.my_bookings,name='my_bookings'),
    path('provider/dashboard/',views.provider_dashboard,name='provider_dashboard'),
    path('booking/<int:id>/accept/',views.accept_booking,name='accept_booking'),
    path('booking/<int:id>/reject/',views.reject_booking,name='reject_booking'),
    path('booking/<int:id>/complete/',views.complete_booking,name='complete_booking'),
    path('review/<int:booking_id>/',views.add_review,name='add_review'),
    path('booking/<int:id>/cancel/',views.cancel_booking,name='cancel_booking'),
]