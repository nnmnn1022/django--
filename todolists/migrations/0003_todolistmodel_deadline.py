# Generated by Django 3.2.13 on 2022-05-30 07:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todolists', '0002_auto_20220524_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolistmodel',
            name='deadline',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='기한'),
            preserve_default=False,
        ),
    ]
