# Generated by Django 3.0.3 on 2020-03-02 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empapi', '0002_auto_20200302_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='status_code',
            field=models.IntegerField(default=0),
        ),
    ]
