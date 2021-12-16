# Generated by Django 3.1.5 on 2021-12-16 05:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('problemlist', '0002_remove_problem_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='problemlist', to=settings.AUTH_USER_MODEL),
        ),
    ]
