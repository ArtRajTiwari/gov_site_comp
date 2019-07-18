# Generated by Django 2.2.2 on 2019-06-23 02:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gov_site_app', '0028_suchanaitems_suchana_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='suchanaitems',
            old_name='Suchana_date',
            new_name='Suchana1_date',
        ),
        migrations.AddField(
            model_name='suchanaitems',
            name='Suchana2_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='suchanaitems',
            name='Suchana3_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
