# Generated by Django 3.1.7 on 2021-03-13 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0004_auto_20210313_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='sex',
            field=models.IntegerField(choices=[(1, 'Nam'), (0, 'Nữ')], default=0),
        ),
    ]