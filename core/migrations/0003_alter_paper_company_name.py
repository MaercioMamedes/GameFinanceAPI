# Generated by Django 3.2 on 2023-02-16 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_wallet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='company_name',
            field=models.CharField(max_length=100, verbose_name='Nome da empresa'),
        ),
    ]