# Generated by Django 4.0.1 on 2022-01-15 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_detail_question_userans_payment_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='options',
            name='qans4',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='userans',
            name='qans4',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
