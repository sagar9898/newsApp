# Generated by Django 2.2.5 on 2019-10-11 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20191008_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='tag',
            field=models.TextField(default=''),
        ),
    ]
