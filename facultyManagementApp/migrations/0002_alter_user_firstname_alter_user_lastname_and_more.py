# Generated by Django 4.1.4 on 2022-12-08 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facultyManagementApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='firstName',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='lastName',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='userLevel',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
