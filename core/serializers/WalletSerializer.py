from rest_framework import serializers
from core.models import Wallet


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['paper']

    def create(self, validated_data):
        user = self.context.get('request').user
        user_paper_qtd = Wallet.objects.filter(user=user.id)
        if len(user_paper_qtd) >= 5:
            raise serializers.ValidationError('o usuário já possui 5 papéis na carteira')

        return Wallet.objects.create(
            user=user,
            paper=validated_data['paper'],
        )
