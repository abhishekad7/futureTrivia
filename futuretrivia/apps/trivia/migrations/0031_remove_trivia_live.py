# Generated by Django 2.1.1 on 2018-10-22 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0030_auto_20181019_0508'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trivia',
            name='live',
        ),
    ]