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
        global date
        representation = super().to_representation(instance)
        print('11111111111111111111')
        print(self.instance.first())
        data = self.instance.values().last()
        print(data)
        date1 = data['date'].date()
        representation['date'] = date1
        return representation
