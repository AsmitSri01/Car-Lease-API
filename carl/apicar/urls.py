from django.urls import path
from .views import lease_car , drop_car , filter_cars

urlpatterns=[
    path('api/car/lease',lease_car),
    path('api/car/drop',drop_car),
    path('api/car/<filter>',filter_cars)
]