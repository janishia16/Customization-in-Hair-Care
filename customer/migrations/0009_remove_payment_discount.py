# Generated by Django 4.0.1 on 2022-01-17 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_alter_detail_pid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='discount',
        ),
    ]
