# Generated by Django 4.1.7 on 2023-04-13 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CallAnalitics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phones', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('time', models.TimeField()),
                ('status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phones', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('number_calls', models.IntegerField()),
                ('retry_count', models.IntegerField()),
                ('repeated_time', models.IntegerField()),
            ],
        ),
    ]
