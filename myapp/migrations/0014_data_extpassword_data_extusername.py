# Generated by Django 4.1.7 on 2023-05-05 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_data_verification_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='extpassword',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='data',
            name='extusername',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
