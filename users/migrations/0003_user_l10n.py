# Generated by Django 3.2.13 on 2022-05-30 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='l10n',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='담당 언어'),
        ),
    ]
