# Generated by Django 5.1.7 on 2025-04-07 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='This is an awesome blog', max_length=255),
        ),
    ]
