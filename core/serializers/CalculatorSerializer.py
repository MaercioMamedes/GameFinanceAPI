from rest_framework import serializers


class CalculatorSerializer(serializers.Serializer):
    period = (
        ('teste','olá mundo'),
        ('teste2', '1mo')
    )
    teste = serializers.ChoiceField(choices=period)

    def validate(self, data):
        if not data['teste']:
            raise serializers.ValidationError("atribudo errado")
        return data
