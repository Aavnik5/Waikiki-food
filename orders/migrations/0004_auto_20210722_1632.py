# Generated by Django 3.2.5 on 2021-07-22 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_cartitems_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='razor_pay_order_id',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='razorpay_payment_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='razorpay_signature',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]