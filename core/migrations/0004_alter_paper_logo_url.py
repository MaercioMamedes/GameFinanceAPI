# Generated by Django 3.2 on 2023-02-16 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_paper_company_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='logo_url',
            field=models.CharField(max_length=200),
        ),
    ]
