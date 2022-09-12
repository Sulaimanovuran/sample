from rest_framework import serializers

from schedule.models import Scroll, Date


class ScrollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scroll
        fields = '__all__'


class DateSerializer(serializers.Serializer):
    date = serializers.DateTimeField(required=True)

