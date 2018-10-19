# Generated by Django 2.1.1 on 2018-09-13 22:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Trivia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=20, unique=True)),
                ('rated', models.BooleanField(default=False)),
                ('private', models.BooleanField(default=False)),
                ('category', models.CharField(default='General', max_length=100)),
                ('prize', models.TextField(default='Not Declared', max_length=500)),
                ('about', models.TextField(default='No details.', max_length=1000)),
                ('announcements', models.TextField(default='No Announcements', max_length=500)),
                ('start_time', models.DateTimeField()),
                ('duration', models.IntegerField(default=0)),
                ('per_problem_duration', models.IntegerField(default=0)),
                ('can_navigate', models.BooleanField(default=False)),
                ('portal', models.BooleanField(default=True)),
                ('positive_score', models.IntegerField()),
                ('negative_score', models.IntegerField()),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]