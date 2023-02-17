from rest_framework import viewsets
from core.serializers import WalletSerializer
from core.models import Wallet
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class WalletViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        return Wallet.objects.filter(user=self.request.user.id)
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = WalletSerializer
