# Generated by Django 4.0.6 on 2022-12-01 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0007_remove_customersignup_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='customersignup',
            name='phone',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
    ]
