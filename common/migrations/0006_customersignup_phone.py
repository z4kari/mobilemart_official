# Generated by Django 4.0.6 on 2022-11-29 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_remove_customersignup_cpswd'),
    ]

    operations = [
        migrations.AddField(
            model_name='customersignup',
            name='phone',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
    ]
