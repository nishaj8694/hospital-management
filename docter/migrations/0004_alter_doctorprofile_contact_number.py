# Generated by Django 4.2 on 2023-05-11 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docter', '0003_remove_doctorprofile_email_vr_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorprofile',
            name='contact_number',
            field=models.CharField(max_length=10, null=True),
        ),
    ]