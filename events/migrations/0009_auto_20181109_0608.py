# Generated by Django 2.0.6 on 2018-11-09 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_auto_20181109_0537'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='announcement',
            new_name='announcements',
        ),
    ]