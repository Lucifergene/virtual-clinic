# Generated by Django 2.1.2 on 2018-10-31 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0011_auto_20181031_0310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='symptom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.Symptom'),
        ),
    ]
