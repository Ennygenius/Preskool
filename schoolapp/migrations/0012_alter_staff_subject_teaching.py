# Generated by Django 3.2.18 on 2023-08-06 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0011_staff_subject_teaching'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='subject_teaching',
            field=models.CharField(choices=[('Mathematics', 'MATHEMATICS'), ('English', 'ENGLISH'), ('Biology', 'BIOLOGY')], default='mathematics', max_length=233),
        ),
    ]
