# Generated by Django 3.1.5 on 2021-12-17 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0002_auto_20211217_0338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='language',
            field=models.TextField(default=0),
        ),
        migrations.AlterField(
            model_name='submission',
            name='user_id',
            field=models.IntegerField(default=-1),
        ),
    ]