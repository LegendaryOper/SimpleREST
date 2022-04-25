from django.urls import path, include
from cars.views import *

urlpatterns = [
    path('car/create/', CarCreateView.as_view()),
    path('all/', CarListView.as_view()),
    path('car/detail/<int:pk>', CarDetailView.as_view()),

]