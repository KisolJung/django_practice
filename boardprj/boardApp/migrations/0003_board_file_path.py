# Generated by Django 3.2.5 on 2021-07-19 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardApp', '0002_alter_board_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='file_path',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]