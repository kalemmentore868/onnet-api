# Generated by Django 4.1.5 on 2023-01-11 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_client_email_alter_client_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='client',
            name='subject',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]