# Generated by Django 2.2.1 on 2019-05-04 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='photo_1',
            field=models.ImageField(blank=True, upload_to='product/%y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='product',
            name='photo_2',
            field=models.ImageField(blank=True, upload_to='product/%y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='product',
            name='photo_3',
            field=models.ImageField(blank=True, upload_to='product/%y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='product',
            name='photo_4',
            field=models.ImageField(blank=True, upload_to='product/%y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='product',
            name='photo_5',
            field=models.ImageField(blank=True, upload_to='product/%y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='product',
            name='photo_6',
            field=models.ImageField(blank=True, upload_to='product/%y/%m/%d/'),
        ),
    ]