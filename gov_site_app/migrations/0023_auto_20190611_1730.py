# Generated by Django 2.2.1 on 2019-06-11 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gov_site_app', '0022_organizationdetail_wadanumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizationdetail',
            name='wadaNumber',
            field=models.IntegerField(),
        ),
    ]
