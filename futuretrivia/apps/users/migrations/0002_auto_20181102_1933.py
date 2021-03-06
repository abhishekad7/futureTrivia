# Generated by Django 2.1.1 on 2018-11-02 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetails',
            name='last_active',
        ),
        migrations.RemoveField(
            model_name='userdetails',
            name='security_answer',
        ),
        migrations.RemoveField(
            model_name='userdetails',
            name='security_question',
        ),
        migrations.AddField(
            model_name='userdetails',
            name='confirm_token',
            field=models.CharField(blank=True, default='', max_length=256),
        ),
        migrations.AddField(
            model_name='userdetails',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userdetails',
            name='emails',
            field=models.TextField(default='{}'),
        ),
    ]
