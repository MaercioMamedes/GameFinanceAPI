from rest_framework import serializers
from core.models import Paper
from core.helpers import DataApiFinancePaper


class PaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paper
        fields = ['id','b3_code','company_name', 'last_value','logo_url']
        extra_kwargs = {
                        'id':{'read_only': True},
                        'company_name': {'read_only': True},
                        'last_value': {'read_only': True},
                        'logo_url': {'read_only': True},
        }

    def create(self, validated_data):
        api = DataApiFinancePaper(validated_data['b3_code'])
        return api.create_paper()


