# Generated by Django 4.2.4 on 2023-09-04 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0007_turflocation_tname'),
        ('Manager', '0003_managerregister_assignedturf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='managerregister',
            name='assignedturf',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Admin.turflocation'),
        ),
    ]
