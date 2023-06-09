# Generated by Django 4.2 on 2023-05-05 06:42

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admn', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_patient', models.BooleanField(default=False)),
                ('is_docter', models.BooleanField(default=False)),
                ('block', models.BooleanField(default=False)),
                ('f_passw', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_date', models.DateField(blank=True, null=True)),
                ('appointment_time', models.TimeField(blank=True, null=True)),
                ('reason', models.TextField(max_length=500)),
                ('status', models.CharField(blank=True, choices=[('Pending', 'Pending'), ('accept', 'accept'), ('reject', 'reject'), ('finish', 'finish')], default='pending', max_length=10, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Total_Price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('Pay_option', models.CharField(max_length=10, null=True)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(blank=True, choices=[('Pending', 'Pending'), ('shiped', 'shiped'), ('deliverd', 'deliverd'), ('cancel', 'cancel')], default='pending', max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='treatment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symtems', models.TextField(max_length=500)),
                ('ordstatus', models.BooleanField(default=False)),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='OP', to='home.appointment')),
            ],
        ),
        migrations.CreateModel(
            name='TreatMedicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('Treatment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='treat', to='home.treatment')),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sup', to='admn.varient')),
            ],
        ),
        migrations.CreateModel(
            name='Refund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('refund_option', models.CharField(blank=True, choices=[('bank', 'bank'), ('wallet', 'wallet')], default='wallet', max_length=10, null=True)),
                ('refund_reason', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.CharField(blank=True, choices=[('Pending', 'Pending'), ('cancel', 'cancel'), ('completed', 'completed')], default='pending', max_length=10, null=True)),
                ('cancelby', models.CharField(blank=True, choices=[('admin', 'admin'), ('user', 'user')], default='none', max_length=100, null=True)),
                ('refund_amount', models.PositiveIntegerField(blank=True, null=True)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.order')),
            ],
        ),
        migrations.CreateModel(
            name='orderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='home.order')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admn.product')),
            ],
        ),
    ]
