# Generated by Django 2.2.5 on 2019-10-29 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_news_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='act',
            field=models.IntegerField(default=0),
        ),
    ]
