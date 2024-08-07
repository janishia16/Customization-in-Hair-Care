# Generated by Django 4.0.1 on 2022-03-28 10:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer', '0014_alter_order_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Human (Default)', max_length=200, null=True)),
                ('title', models.CharField(default='This is the default,title change it in profile.', max_length=200, null=True)),
                ('desc', models.CharField(default='Hey,there this is a default text description about you that you change.', max_length=200, null=True)),
                ('profile_img', models.ImageField(blank=True, default='media/default.jpg', null=True, upload_to='pics')),
                ('email', models.EmailField(max_length=30)),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
