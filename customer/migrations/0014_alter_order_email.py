# Generated by Django 4.0.1 on 2022-01-19 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0013_alter_userans_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
