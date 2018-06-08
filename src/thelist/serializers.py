from rest_framework import serializers

from . models import Client, Order


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = [
            'pk',
            'name',
        ]


class OrderSerializer(serializers.ModelSerializer):
    client_obj = ClientSerializer(source='client', read_only=True)
    class Meta:
        model = Order
        fields = [
            'pk',
            'amount',
            'item',
            'client',
            'client_obj',
        ]