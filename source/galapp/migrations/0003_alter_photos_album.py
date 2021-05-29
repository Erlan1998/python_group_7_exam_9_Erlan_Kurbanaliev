# Generated by Django 3.2.3 on 2021-05-29 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('galapp', '0002_alter_photos_album'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='album',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Photos', to='galapp.albom', verbose_name='фото'),
        ),
    ]
