from django.shortcuts import render
from django_filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework import mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from schedule.models import Scroll, Date
from schedule.serializers import ScrollSerializer, DateSerializer


class ScrollView(ModelViewSet):
    queryset = Scroll.objects.all()
    serializer_class = ScrollSerializer


class DateView(mixins.CreateModelMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = Date.objects.all()
    serializer_class = DateSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['date']
