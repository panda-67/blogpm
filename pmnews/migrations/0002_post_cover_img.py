# Generated by Django 3.2.5 on 2021-07-21 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pmnews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cover_img',
            field=models.ImageField(null=True, upload_to='cover/'),
        ),
    ]
