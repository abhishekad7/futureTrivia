# Generated by Django 2.1.1 on 2018-10-27 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0037_auto_20181027_0659'),
    ]

    operations = [
        migrations.AddField(
            model_name='triviaresult',
            name='feedback',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='trivia',
            name='rating',
            field=models.TextField(default='0,0,0,0,0'),
        ),
    ]