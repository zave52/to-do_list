# Generated by Django 5.1.5 on 2025-01-14 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='name',
        ),
        migrations.AlterField(
            model_name='task',
            name='content',
            field=models.CharField(max_length=255),
        ),
    ]
