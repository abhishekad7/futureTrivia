# Generated by Django 2.1.1 on 2018-10-09 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0018_triviaresult_modified_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='trivia',
            name='per_questions_duration',
            field=models.IntegerField(default=0),
        ),
    ]
