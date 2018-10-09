# Generated by Django 2.1.1 on 2018-10-08 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0012_auto_20181008_1400'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trivia',
            name='negative_score',
        ),
        migrations.RemoveField(
            model_name='trivia',
            name='positive_score',
        ),
        migrations.AddField(
            model_name='question',
            name='negative_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='positive_score',
            field=models.IntegerField(default=0),
        ),
    ]
