from core.models import Wallet
from django.contrib.auth.models import User
from django.db import models


class UserWallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    initial_value = models.DecimalField('valor inicial da carteira', max_digits=8, decimal_places=2)
    final_value = models.DecimalField('valor inicial da carteira', max_digits=8, decimal_places=2)
    profit = models.DecimalField('Lucro', max_digits=4, decimal_places=2)
