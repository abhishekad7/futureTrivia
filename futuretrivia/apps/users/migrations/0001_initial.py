# Generated by Django 2.1.1 on 2018-11-02 19:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trivia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('security_question', models.CharField(blank=True, max_length=100, null=True)),
                ('security_answer', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, default='India', max_length=100, null=True)),
                ('last_active', models.DateTimeField(blank=True, null=True)),
                ('trivias', models.ManyToManyField(to='trivia.Trivia')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
