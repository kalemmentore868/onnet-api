from rest_framework import serializers
from .models import Client

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Client
        fields=('first_name','last_name', 'phone', 'subject', 'message', 'email' )