# Generated by Django 2.2.5 on 2019-10-08 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_news_ocatid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='name',
            field=models.CharField(max_length=150),
        ),
    ]
