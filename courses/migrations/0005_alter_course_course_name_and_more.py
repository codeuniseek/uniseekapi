# Generated by Django 5.0.3 on 2024-03-26 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_course_range_tution_fee_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='earliest_intake',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
