# Generated by Django 4.1.3 on 2022-11-14 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='content',
            field=models.TextField(default='Please, fill me in'),
        ),
    ]
