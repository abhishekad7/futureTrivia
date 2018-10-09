# Generated by Django 2.1.1 on 2018-09-18 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0006_auto_20180916_1112'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('mcq', models.BooleanField(default=True)),
                ('options', models.TextField(blank=True, null=True)),
                ('correct_answer', models.TextField()),
                ('explaination', models.TextField(default='No explaination')),
                ('trivia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trivia.Trivia')),
            ],
        ),
    ]
