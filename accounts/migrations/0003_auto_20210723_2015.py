# Generated by Django 3.2.5 on 2021-07-23 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210723_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cusomeraddress',
            name='address',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='cusomeraddress',
            name='pincode',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
