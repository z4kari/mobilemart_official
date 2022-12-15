# Generated by Django 4.0.6 on 2022-12-01 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_admin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='addmobile',
            name='Price',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='addmobile',
            name='description',
            field=models.CharField(default='as', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='addmobile',
            name='marketPrice',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='addmobile',
            name='qty',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
    ]