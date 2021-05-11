# Generated by Django 3.2.2 on 2021-05-10 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_metric_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='metric',
            name='value',
        ),
        migrations.AddField(
            model_name='weather',
            name='value',
            field=models.FloatField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
