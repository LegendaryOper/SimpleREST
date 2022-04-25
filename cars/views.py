
from rest_framework import generics
from cars.serializers import *
from cars.models import Car
from cars.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
# Create your views here.


class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer
    permission_classes = (IsAdminUser, )


class CarListView(generics.ListAPIView):
    serializer_class = CarListSerializer
    queryset = Car.objects.all()
    permission_classes = (IsAuthenticated, )


class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )
    authentication_classes = (TokenAuthentication, )
