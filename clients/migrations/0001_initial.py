# Generated by Django 4.1.5 on 2023-01-06 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('number', models.IntegerField()),
                ('subject', models.CharField(max_length=200)),
                ('message', models.CharField(max_length=700)),
            ],
        ),
    ]