# Generated by Django 3.0.3 on 2020-03-15 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empapi', '0009_uploadimagetest'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelWithImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]
