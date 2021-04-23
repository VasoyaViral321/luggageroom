from rest_framework import serializers
from login.models import Customer
from booking.models import Booking,Storages
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id','username', 'password', 'email', 'state','pin_code','address','profile_pic']
class StoragesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storages
        fields = ['id','manager', 'state_name', 'city_name', 'is_available','price','storage_location','start_date','room_image']
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id','city_name', 'user_id', 'start_day', 'end_day','amount','booked_on']