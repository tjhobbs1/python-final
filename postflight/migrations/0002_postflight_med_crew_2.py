# Generated by Django 2.2.8 on 2019-12-06 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postflight', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postflight',
            name='med_crew_2',
            field=models.CharField(default='', max_length=100),
        ),
    ]
