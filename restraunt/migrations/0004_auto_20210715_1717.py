# Generated by Django 3.2.5 on 2021-07-15 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restraunt', '0003_restraunt_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restraunt',
            name='restraunt_image',
            field=models.ImageField(blank=True, null=True, upload_to='restraunts_name'),
        ),
        migrations.AlterField(
            model_name='restrauntmenu',
            name='menu_image',
            field=models.ImageField(blank=True, null=True, upload_to='restraunt_menu'),
        ),
    ]
