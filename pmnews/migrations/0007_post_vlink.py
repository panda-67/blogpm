# Generated by Django 3.2.7 on 2021-09-24 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pmnews', '0006_auto_20210919_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='vlink',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
