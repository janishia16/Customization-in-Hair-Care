# Generated by Django 4.0.1 on 2022-01-19 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0012_alter_userans_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userans',
            name='username',
            field=models.CharField(max_length=200),
        ),
    ]
