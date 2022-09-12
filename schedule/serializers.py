from rest_framework import serializers

from schedule.models import Scroll, Date


class ScrollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scroll
        fields = '__all__'


class DateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Date
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['employee'] = self.instance
        data = self.instance.values().last()
        representation['time'] = data['date'].time()
        date1 = data['date'].date()
        representation['date'] = date1
        return representation
