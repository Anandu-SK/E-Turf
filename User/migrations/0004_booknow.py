# Generated by Django 4.2.4 on 2023-09-06 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_timerange'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booknow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ubookingname', models.CharField(max_length=50, null=True)),
                ('ubookingemail', models.EmailField(max_length=50, null=True)),
                ('ubookingphone', models.CharField(max_length=50, null=True)),
                ('ubookingcategory', models.CharField(max_length=50, null=True)),
                ('ubookingprice', models.CharField(max_length=50, null=True)),
                ('uboookingaddress', models.CharField(max_length=50, null=True)),
                ('ubookingdate', models.DateField(max_length=50, null=True)),
                ('bookingtime', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
