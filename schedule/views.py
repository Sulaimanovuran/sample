from django.shortcuts import render
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
