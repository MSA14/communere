# Generated by Django 4.1 on 2022-10-01 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0002_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='rolecategory',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]