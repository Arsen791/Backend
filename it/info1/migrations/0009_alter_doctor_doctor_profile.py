# Generated by Django 4.1.2 on 2023-04-16 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info1', '0008_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='doctor_profile',
            field=models.BooleanField(null=True),
        ),
    ]