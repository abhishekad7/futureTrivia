# Generated by Django 2.1.1 on 2018-10-25 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0034_auto_20181025_0535'),
    ]

    operations = [
        migrations.AddField(
            model_name='trivia',
            name='locked',
            field=models.BooleanField(default=False),
        ),
    ]