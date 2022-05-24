# Generated by Django 3.2.13 on 2022-05-24 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolists', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolistmodel',
            name='modified_at',
            field=models.DateTimeField(auto_now=True, verbose_name='수정일시'),
        ),
        migrations.AlterField(
            model_name='todolistmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='생성일시'),
        ),
    ]