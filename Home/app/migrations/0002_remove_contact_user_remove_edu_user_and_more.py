# Generated by Django 4.1.6 on 2023-02-06 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='user',
        ),
        migrations.RemoveField(
            model_name='edu',
            name='user',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='user',
        ),
        migrations.RemoveField(
            model_name='interest',
            name='user',
        ),
        migrations.RemoveField(
            model_name='language',
            name='user',
        ),
        migrations.RemoveField(
            model_name='project',
            name='user',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='user',
        ),
        migrations.AddField(
            model_name='profile',
            name='contacts',
            field=models.ManyToManyField(to='app.contact'),
        ),
        migrations.AddField(
            model_name='profile',
            name='edus',
            field=models.ManyToManyField(to='app.edu'),
        ),
        migrations.AddField(
            model_name='profile',
            name='experiences',
            field=models.ManyToManyField(to='app.experience'),
        ),
        migrations.AddField(
            model_name='profile',
            name='interests',
            field=models.ManyToManyField(to='app.interest'),
        ),
        migrations.AddField(
            model_name='profile',
            name='languages',
            field=models.ManyToManyField(to='app.language'),
        ),
        migrations.AddField(
            model_name='profile',
            name='projects',
            field=models.ManyToManyField(to='app.project'),
        ),
        migrations.AddField(
            model_name='profile',
            name='skills',
            field=models.ManyToManyField(to='app.skill'),
        ),
    ]