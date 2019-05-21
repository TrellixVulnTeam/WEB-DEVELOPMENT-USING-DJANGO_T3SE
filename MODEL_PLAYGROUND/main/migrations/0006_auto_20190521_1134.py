# Generated by Django 2.2.1 on 2019-05-21 06:04

import django.core.validators
from django.db import migrations, models
import main.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_student_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(150), django.core.validators.MinValueValidator(0), main.validators.validate_even_number]),
        ),
    ]
