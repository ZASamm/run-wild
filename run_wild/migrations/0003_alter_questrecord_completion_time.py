# Generated by Django 4.2.16 on 2024-11-28 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('run_wild', '0002_auto_20241128_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questrecord',
            name='completion_time',
            field=models.DurationField(),
        ),
    ]
