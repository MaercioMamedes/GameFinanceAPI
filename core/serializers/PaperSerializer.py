from rest_framework import serializers
from core.models import Paper
from core.helpers import DataApiFinancePaper


class PaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paper
        fields = ['b3_code']

    def create(self, validated_data):
        api = DataApiFinancePaper(validated_data['b3_code'])
        return api.create_paper()


