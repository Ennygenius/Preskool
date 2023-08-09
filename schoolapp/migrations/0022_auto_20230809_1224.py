# Generated by Django 3.2.18 on 2023-08-09 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0021_staff_joining_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='city',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='country',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='expreience',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='qualifications',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='state',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='zip_code',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]