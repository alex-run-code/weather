# Generated by Django 3.2.2 on 2021-05-11 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20210511_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weather',
            name='location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.location'),
            preserve_default=False,
        ),
    ]
