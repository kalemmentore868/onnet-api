# Generated by Django 4.1.5 on 2023-01-10 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='email',
            field=models.CharField(default='lem@gmail.com', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='client',
            name='number',
            field=models.CharField(max_length=100),
        ),
    ]
