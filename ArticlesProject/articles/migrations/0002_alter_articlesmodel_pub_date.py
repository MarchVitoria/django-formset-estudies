# Generated by Django 4.2 on 2023-11-16 20:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlesmodel',
            name='pub_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 11, 16, 20, 53, 9, 818969, tzinfo=datetime.timezone.utc)),
        ),
    ]
