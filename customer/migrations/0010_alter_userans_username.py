# Generated by Django 4.0.1 on 2022-01-19 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0009_remove_payment_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userans',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.register'),
        ),
    ]