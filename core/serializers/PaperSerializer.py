from rest_framework import serializers
from core.models import Paper
from core.helpers import DataApiFinancePaper


class PaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paper
        fields = ['id','b3_code','company_name', 'first_value','last_value']
        extra_kwargs = {
                        'id':{'read_only': True},
                        'last_value': {'read_only': True},
                        'first_value': {'read_only': True},
        }

    def create(self, validated_data):
        api = DataApiFinancePaper(validated_data['b3_code'], validated_data['company_name'])
        return api.create_paper()


