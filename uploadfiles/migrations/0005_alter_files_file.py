# Generated by Django 4.0.1 on 2022-07-14 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploadfiles', '0004_files'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
