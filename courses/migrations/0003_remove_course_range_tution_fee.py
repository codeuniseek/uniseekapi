# Generated by Django 5.0.3 on 2024-03-26 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_range_tution_fee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='range_tution_fee',
        ),
    ]