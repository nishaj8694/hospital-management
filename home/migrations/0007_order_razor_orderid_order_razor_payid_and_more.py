# Generated by Django 4.2 on 2023-05-06 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_order_discount_restriction'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='razor_orderid',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='razor_payid',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='razor_signature',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
