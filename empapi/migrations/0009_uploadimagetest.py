# Generated by Django 3.0.3 on 2020-03-15 07:17

from django.db import migrations, models
import empapi.models


class Migration(migrations.Migration):

    dependencies = [
        ('empapi', '0008_sessionmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadImageTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, max_length=254, null=True, upload_to=empapi.models.nameFile)),
            ],
        ),
    ]
