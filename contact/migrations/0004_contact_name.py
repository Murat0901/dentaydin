# Generated by Django 3.0.5 on 2020-05-03 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_remove_contact_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=50, null=True, verbose_name='Ad Soyad'),
        ),
    ]
