# Generated by Django 2.2.3 on 2019-07-24 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gov_site_app', '0029_auto_20190623_0258'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sewa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('descriptionOfImage', models.TextField(default='Title', max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='suchanaitems',
            name='Suchana1_suchana_info',
            field=models.TextField(blank=True, default='Title', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='suchanaitems',
            name='Suchana2_suchana_info',
            field=models.TextField(blank=True, default='Title', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='suchanaitems',
            name='Suchana3_suchana_info',
            field=models.TextField(blank=True, default='Title', max_length=250, null=True),
        ),
    ]
