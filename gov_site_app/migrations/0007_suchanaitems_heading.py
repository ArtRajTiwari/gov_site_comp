# Generated by Django 2.2 on 2019-05-28 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gov_site_app', '0006_suchanaphotogallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='suchanaitems',
            name='heading',
            field=models.CharField(default='Title', max_length=32),
        ),
    ]
