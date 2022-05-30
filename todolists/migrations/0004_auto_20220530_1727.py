# Generated by Django 3.2.13 on 2022-05-30 08:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todolists', '0003_todolistmodel_deadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolistmodel',
            name='worker',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='worker', to='users.user', verbose_name='담당자'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='todolistmodel',
            name='created_by',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='todolist_writer', to='todolists.todolistmodel', verbose_name='작성자'),
        ),
    ]