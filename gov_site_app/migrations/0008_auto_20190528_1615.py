# Generated by Django 2.2 on 2019-05-28 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gov_site_app', '0007_suchanaitems_heading'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suchanaitems',
            name='suchana_photo_description',
            field=models.TextField(max_length=200),
        ),
    ]
