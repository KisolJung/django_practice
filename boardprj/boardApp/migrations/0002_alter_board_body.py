# Generated by Django 3.2.5 on 2021-07-23 08:54

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boardApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
