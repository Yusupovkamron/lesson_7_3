# Generated by Django 5.0.4 on 2024-05-09 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_remove_albom_cover_albom_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='country',
            old_name='cover',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='albom',
            name='address',
        ),
        migrations.AddField(
            model_name='albom',
            name='cover',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='country',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]
