# Generated by Django 3.2.3 on 2021-05-29 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galapp', '0004_photos_is_private'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='is_private',
            field=models.BooleanField(default=False, verbose_name='приватный'),
        ),
    ]