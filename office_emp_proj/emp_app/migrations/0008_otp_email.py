# Generated by Django 5.0.6 on 2024-06-19 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0007_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='otp',
            name='Email',
            field=models.EmailField(default=None, max_length=254),
        ),
    ]