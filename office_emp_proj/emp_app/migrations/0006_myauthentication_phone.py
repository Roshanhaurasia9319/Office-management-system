# Generated by Django 5.0.6 on 2024-06-15 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0005_alter_myauthentication_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='myauthentication',
            name='Phone',
            field=models.CharField(default=None, max_length=10),
        ),
    ]