# Generated by Django 2.2.2 on 2019-06-22 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gov_site_app', '0024_auto_20190622_0535'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photogallery',
            old_name='descriptionOfImage1',
            new_name='descriptionOfImage',
        ),
        migrations.RenameField(
            model_name='photogallery',
            old_name='image1',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='photogallery',
            old_name='title_of_photo1',
            new_name='title_of_photo',
        ),
        migrations.RemoveField(
            model_name='photogallery',
            name='descriptionOfImage2',
        ),
        migrations.RemoveField(
            model_name='photogallery',
            name='descriptionOfImage3',
        ),
        migrations.RemoveField(
            model_name='photogallery',
            name='descriptionOfImage4',
        ),
        migrations.RemoveField(
            model_name='photogallery',
            name='descriptionOfImage5',
        ),
        migrations.RemoveField(
            model_name='photogallery',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='photogallery',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='photogallery',
            name='image4',
        ),
        migrations.RemoveField(
            model_name='photogallery',
            name='image5',
        ),
        migrations.RemoveField(
            model_name='photogallery',
            name='title_of_photo2',
        ),
        migrations.RemoveField(
            model_name='photogallery',
            name='title_of_photo3',
        ),
        migrations.RemoveField(
            model_name='photogallery',
            name='title_of_photo4',
        ),
        migrations.RemoveField(
            model_name='photogallery',
            name='title_of_photo5',
        ),
    ]