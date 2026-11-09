from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('providers/',views.provider_list,name='provider_list'),
    path('providers/<int:id>/',views.provider_detail,name='provider_detail'),
]