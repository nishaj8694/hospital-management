# Generated by Django 4.2 on 2023-05-09 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientprofile',
            name='is_verify',
            field=models.BooleanField(default=False),
        ),
    ]
