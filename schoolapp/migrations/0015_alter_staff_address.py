# Generated by Django 3.2.18 on 2023-08-07 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0014_staff_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
