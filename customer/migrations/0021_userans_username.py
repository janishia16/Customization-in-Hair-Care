# Generated by Django 4.0.1 on 2022-03-28 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0020_remove_userans_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='userans',
            name='username',
            field=models.CharField(default='exit', max_length=200),
            preserve_default=False,
        ),
    ]