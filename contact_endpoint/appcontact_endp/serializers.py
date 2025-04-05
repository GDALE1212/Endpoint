from rest_framework.serializers import ModelSerializer
from .models import Contacts

class contact_serializer(ModelSerializer):
    class Meta:
        model = Contacts
        
        fields  = (
            'name',
            'address',
            'phone_number',
            'hotline',
            'category'
        )