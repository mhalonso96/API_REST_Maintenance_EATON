# Generated by Django 4.2.2 on 2023-06-23 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0002_maintenance_created_at_maintenance_departament_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenance',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
