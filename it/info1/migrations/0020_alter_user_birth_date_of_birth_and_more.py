# Generated by Django 4.1.2 on 2023-04-22 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info1', '0019_alter_employee_options_remove_employee_position_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_birth',
            name='date_of_birth',
            field=models.DateField(default=' ', null=True),
        ),
        migrations.AlterField(
            model_name='user_birth',
            name='place_of_birth',
            field=models.CharField(default=' ', max_length=255),
        ),
        migrations.AlterField(
            model_name='user_name',
            name='firstname',
            field=models.CharField(default=' ', max_length=255),
        ),
        migrations.AlterField(
            model_name='user_name',
            name='secondname',
            field=models.CharField(default=' ', max_length=255),
        ),
    ]
