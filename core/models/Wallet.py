from django.db import models
from django.contrib.auth.models import User
from core.models import Paper


class Wallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE)
