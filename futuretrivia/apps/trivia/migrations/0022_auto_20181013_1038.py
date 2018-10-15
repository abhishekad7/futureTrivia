# Generated by Django 2.1.1 on 2018-10-13 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0021_auto_20181010_0547'),
    ]

    operations = [
        migrations.RenameField(
            model_name='triviaresult',
            old_name='score',
            new_name='negative_score',
        ),
        migrations.AddField(
            model_name='triviaresult',
            name='positive_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='triviaresult',
            name='time_taken',
            field=models.IntegerField(default=0),
        ),
    ]
