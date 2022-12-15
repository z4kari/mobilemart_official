# Generated by Django 4.0.6 on 2022-12-01 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddMobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobileName', models.CharField(max_length=100)),
                ('brandName', models.CharField(max_length=100)),
                ('networkProvider', models.CharField(max_length=100)),
                ('os', models.CharField(max_length=100)),
                ('cellularTechnology', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('processor', models.CharField(max_length=100)),
                ('display', models.CharField(max_length=100)),
                ('frontImage', models.ImageField(upload_to='')),
                ('backImage', models.ImageField(upload_to='')),
                ('leftImage', models.ImageField(upload_to='')),
                ('rightImage', models.ImageField(upload_to='')),
            ],
        ),
    ]