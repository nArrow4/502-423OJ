# Generated by Django 3.1.5 on 2021-12-20 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0004_auto_20211220_0704'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='submission',
            options={'ordering': ['-submit_time']},
        ),
    ]
