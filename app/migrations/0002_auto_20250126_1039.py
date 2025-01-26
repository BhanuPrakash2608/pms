# Generated by Django 3.2.21 on 2025-01-26 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='github_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='github_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
