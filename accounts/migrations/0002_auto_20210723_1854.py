# Generated by Django 3.2.5 on 2021-07-23 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cusomeraddress',
            name='country',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cusomeraddress',
            name='state',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
