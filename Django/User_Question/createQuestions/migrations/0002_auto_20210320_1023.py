# Generated by Django 3.1.7 on 2021-03-20 03:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('createQuestions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='name_question',
            new_name='question',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='name_question',
            new_name='question',
        ),
        migrations.AddField(
            model_name='question',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 20, 3, 23, 21, 440617, tzinfo=utc)),
        ),
    ]
