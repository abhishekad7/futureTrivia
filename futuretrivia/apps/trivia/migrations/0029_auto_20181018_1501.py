# Generated by Django 2.1.1 on 2018-10-18 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0028_trivia_ready'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trivia',
            name='about',
            field=models.TextField(default='No details.', max_length=5000),
        ),
        migrations.AlterField(
            model_name='trivia',
            name='announcements',
            field=models.TextField(default='No Announcements', max_length=5000),
        ),
        migrations.AlterField(
            model_name='trivia',
            name='prize',
            field=models.TextField(default='Not Declared', max_length=5000),
        ),
    ]