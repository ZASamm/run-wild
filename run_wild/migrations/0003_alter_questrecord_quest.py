# Generated by Django 4.2.16 on 2024-11-26 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('run_wild', '0002_questrecord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questrecord',
            name='quest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quest_records', to='run_wild.questpost'),
        ),
    ]
