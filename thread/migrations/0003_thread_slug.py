# Generated by Django 3.2.6 on 2021-08-22 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thread', '0002_auto_20210822_0408'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]