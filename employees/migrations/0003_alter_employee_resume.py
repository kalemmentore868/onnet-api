# Generated by Django 4.1.5 on 2023-01-14 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_remove_employee_number_employee_email_employee_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='staticfiles/files/'),
        ),
    ]
