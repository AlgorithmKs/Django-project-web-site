# Generated by Django 4.2.7 on 2023-11-07 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='LazyDay', max_length=255),
        ),
    ]
