# Generated by Django 3.2.5 on 2021-07-11 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restraunt', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restraunt',
            name='restraunt_image',
            field=models.ImageField(blank=True, null=True, upload_to='restraunt'),
        ),
        migrations.AddField(
            model_name='restrauntmenu',
            name='menu_image',
            field=models.ImageField(blank=True, null=True, upload_to='menu'),
        ),
    ]
