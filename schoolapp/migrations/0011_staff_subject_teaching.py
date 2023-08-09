# Generated by Django 3.2.18 on 2023-08-06 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0010_staff_is_primary_school_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='subject_teaching',
            field=models.CharField(choices=[('mathematics', 'MATHEMATICS'), ('english', 'ENGLISH'), ('biology', 'BIOLOGY')], default='mathematics', max_length=233),
        ),
    ]
