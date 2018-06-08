from rest_framework import viewsets
from rest_framework import filters

from . models import Order, Client
from . serializers import ClientSerializer, OrderSerializer


class ClientApiView(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = (filters.OrderingFilter, filters.SearchFilter,)
    ordering_fields = (
        'name',
    )
    search_fields = (
        'name',
    )


class OrderApiView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = (filters.OrderingFilter, filters.SearchFilter,)
    ordering_fields = (
        'amount',
        'item',
        'client',
        'client__name'
    )
    search_fields = (
        'amount',
        'item',
        'client__name'
    )
