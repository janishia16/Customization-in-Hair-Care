# Generated by Django 4.0.1 on 2022-01-15 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_rename_delivery_details_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='pid',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]