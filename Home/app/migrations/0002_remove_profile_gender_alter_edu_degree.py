# Generated by Django 4.1.6 on 2023-02-07 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='gender',
        ),
        migrations.AlterField(
            model_name='edu',
            name='degree',
            field=models.CharField(max_length=5),
        ),
    ]