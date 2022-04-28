# Generated by Django 3.1.7 on 2021-03-20 02:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_question', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_answer', models.CharField(max_length=255)),
                ('name_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='createQuestions.question')),
            ],
        ),
    ]
