# Generated by Django 2.0.6 on 2018-07-01 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20180701_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='events/static/events/images'),
        ),
    ]
