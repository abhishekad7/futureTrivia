# Generated by Django 2.1.1 on 2018-09-16 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='country',
            field=models.CharField(blank=True, default='India', max_length=100, null=True),
        ),
    ]
