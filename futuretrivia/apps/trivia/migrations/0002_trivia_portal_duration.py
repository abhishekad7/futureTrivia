# Generated by Django 2.1.1 on 2018-09-14 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trivia',
            name='portal_duration',
            field=models.IntegerField(default=0),
        ),
    ]
