from rest_framework import serializers
from .models import Customer
from users.serializers import UserSerializer

class CustomerSerializer(serializers.ModelSerializer):
    user_details = UserSerializer(source='user', read_only=True)
    
    class Meta:
        model = Customer
        fields = ('id', 'user', 'user_details', 'phone_number', 'address', 'city', 'state', 'country', 'postal_code', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')