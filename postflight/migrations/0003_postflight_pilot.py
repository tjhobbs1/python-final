# Generated by Django 2.2.8 on 2019-12-06 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postflight', '0002_postflight_med_crew_2'),
    ]

    operations = [
        migrations.AddField(
            model_name='postflight',
            name='pilot',
            field=models.CharField(default='', max_length=100),
        ),
    ]
