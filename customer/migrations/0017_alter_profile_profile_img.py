# Generated by Django 4.0.1 on 2022-03-28 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0016_alter_profile_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_img',
            field=models.ImageField(blank=True, default='media/default.jpg', null=True, upload_to='profile'),
        ),
    ]