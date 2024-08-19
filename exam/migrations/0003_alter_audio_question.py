# Generated by Django 5.1 on 2024-08-19 18:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_option_correct_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='audios', to='exam.question', unique=True),
        ),
    ]
