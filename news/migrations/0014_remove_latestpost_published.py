# Generated by Django 3.0.5 on 2020-05-13 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0013_latestpost_published'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='latestpost',
            name='published',
        ),
    ]
