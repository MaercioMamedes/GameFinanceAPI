from core.models import Wallet
from django.contrib.auth.models import User
from django.db import models


class UserWallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    initial_value = models.DecimalField('valor inicial da carteira', max_digits=8, decimal_places=2, default=0)
    final_value = models.DecimalField('valor inicial da carteira', max_digits=8, decimal_places=2, default=0)
    profit = models.DecimalField('Lucro', max_digits=4, decimal_places=2, default=0)

    def wallet_update(self, paper):
        self.initial_value += paper.last_value
