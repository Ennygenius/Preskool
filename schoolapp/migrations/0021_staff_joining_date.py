# Generated by Django 3.2.18 on 2023-08-07 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0020_staff_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='joining_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
