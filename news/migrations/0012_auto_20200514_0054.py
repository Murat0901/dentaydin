# Generated by Django 3.0.5 on 2020-05-13 21:54

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_delete_homemenu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='latestpost',
            name='LatestContent',
            field=ckeditor.fields.RichTextField(verbose_name='İçerik'),
        ),
    ]