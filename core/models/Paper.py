from django.db import models


class Paper(models.Model):
    b3_code = models.CharField('código do Papel', max_length=8, unique=True, blank=False, null=False)
    company_name = models.CharField('Nome da empresa', max_length=100)
    last_value = models.DecimalField('cotação', max_digits=8, decimal_places=2, null=False, blank=False)
    logo_url = models.CharField(max_length=200)

    def __str__(self):
        return self.company_name
