from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from .models import CartItem, Cart, Product, Promotion
from .serializers import CartSerializer


# Create your views here.


class CartViewSet(CreateModelMixin, RetrieveModelMixin,  GenericViewSet):
    queryset = Cart.objects.prefetch_related('items__product').all()
    serializer_class = CartSerializer





