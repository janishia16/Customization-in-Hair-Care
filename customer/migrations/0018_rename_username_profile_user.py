# Generated by Django 4.0.1 on 2022-03-28 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0017_alter_profile_profile_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='username',
            new_name='user',
        ),
    ]
