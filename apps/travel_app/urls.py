from django.urls import path
from . import views

urlpatterns = [

    path('travel/', views.dashboard),
    path('travel/destination/<int:travel_id>', views.destination),
    path('travel/add', views.add),
    path('travel/process_trip', views.process_trip),
    path('travel/join/<int:travel_id>', views.join),
]
