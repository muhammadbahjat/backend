from rest_framework import serializers
from . models import *

class OrderRecievedSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrderRecieved
        fields = ['name', 'phone_number','table_number','item_name']
