# Generated by Django 4.1.5 on 2023-01-11 02:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0004_alter_client_email_alter_client_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='number',
            new_name='phone',
        ),
    ]
