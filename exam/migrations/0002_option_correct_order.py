# Generated by Django 5.1 on 2024-08-19 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='option',
            name='correct_order',
            field=models.IntegerField(default=0),
        ),
    ]
