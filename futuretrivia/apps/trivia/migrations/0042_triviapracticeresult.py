# Generated by Django 2.1.1 on 2018-10-27 22:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trivia', '0041_auto_20181027_1649'),
    ]

    operations = [
        migrations.CreateModel(
            name='TriviaPracticeResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('modified_at', models.DateTimeField(blank=True, null=True)),
                ('time_taken', models.IntegerField(default=0)),
                ('answers', models.TextField(default='{}')),
                ('positive_score', models.IntegerField(default=0)),
                ('negative_score', models.IntegerField(default=0)),
                ('trivia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trivia.Trivia')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
