# Generated by Django 3.1.5 on 2021-12-19 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='error_code',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='result',
            name='score',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='submission',
            name='language',
            field=models.TextField(default='C++'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='user_id',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='usage',
            name='memory',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='usage',
            name='time',
            field=models.IntegerField(default=0),
        ),
    ]
