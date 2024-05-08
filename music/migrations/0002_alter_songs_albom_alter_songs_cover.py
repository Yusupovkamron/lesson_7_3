# Generated by Django 5.0.4 on 2024-05-07 08:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songs',
            name='albom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='music.albom'),
        ),
        migrations.AlterField(
            model_name='songs',
            name='cover',
            field=models.URLField(null=True),
        ),
    ]
