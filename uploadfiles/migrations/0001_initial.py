# Generated by Django 4.0.5 on 2022-07-06 04:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=200)),
                ('uploadedFile', models.FileField(upload_to='')),
                ('dateTimeOfUpload', models.DateTimeField(auto_now=True)),
                ('dateTimeOfStartProcess', models.DateTimeField(null=True)),
                ('dateTimeOfEndProcess', models.DateTimeField(null=True)),
                ('folder', models.CharField(max_length=200, null=True)),
                ('done', models.IntegerField(default=0)),
                ('uploadedFileHash', models.FileField(blank=True, null=True, upload_to='')),
                ('User', models.ForeignKey(blank=True, max_length=10, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(blank=True, max_length=10, null=True, on_delete=django.db.models.deletion.CASCADE, to='uploadfiles.document')),
            ],
            options={
                'ordering': ['-uploadedFile'],
            },
        ),
    ]
