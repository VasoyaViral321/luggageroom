from rest_framework import viewsets
from login.models import Customer
from booking.models import Booking,Storages
from . import serializers

class CustomerViewset(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = serializers.UserSerializer

class StoragesViewset(viewsets.ModelViewSet):
    queryset = Storages.objects.all()
    serializer_class = serializers.StoragesSerializer

class BookingViewset(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = serializers.BookingSerializer