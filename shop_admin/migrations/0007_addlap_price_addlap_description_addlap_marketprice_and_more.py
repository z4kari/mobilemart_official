# Generated by Django 4.0.6 on 2022-12-04 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_admin', '0006_addlap'),
    ]

    operations = [
        migrations.AddField(
            model_name='addlap',
            name='Price',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='addlap',
            name='description',
            field=models.CharField(default='aa', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='addlap',
            name='marketPrice',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='addlap',
            name='qty',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
    ]
