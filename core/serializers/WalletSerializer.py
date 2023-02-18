from rest_framework import serializers
from core.models import Wallet, UserWallet, Paper
from django.shortcuts import get_object_or_404


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['paper']

    def create(self, validated_data):
        user = self.context.get('request').user
        user_paper_qtd = Wallet.objects.filter(user=user.id)
        if len(user_paper_qtd) >= 5:
            raise serializers.ValidationError('o usuário já possui 5 papéis na carteira')

        paper = get_object_or_404(Paper, pk=validated_data['paper'].id)
        user_wallet = get_object_or_404(UserWallet, pk=user.id)

        user_wallet.wallet_update(paper)
        user_wallet.save()

        return Wallet.objects.create(
            user=user,
            paper=validated_data['paper'],
        )
