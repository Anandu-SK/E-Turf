# Generated by Django 4.2.4 on 2023-09-08 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0007_booknow_userid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userfeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, null=True)),
                ('useremail', models.CharField(max_length=50, null=True)),
                ('usersubject', models.CharField(max_length=50, null=True)),
                ('usermessage', models.TextField(max_length=50, null=True)),
            ],
        ),
    ]
