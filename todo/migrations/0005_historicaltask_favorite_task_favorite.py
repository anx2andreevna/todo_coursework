# Generated by Django 4.2.7 on 2024-03-03 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_historicaltask_is_hidden_task_is_hidden'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicaltask',
            name='favorite',
            field=models.BooleanField(default=False, verbose_name='Избранное'),
        ),
        migrations.AddField(
            model_name='task',
            name='favorite',
            field=models.BooleanField(default=False, verbose_name='Избранное'),
        ),
    ]