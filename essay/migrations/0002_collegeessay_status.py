# Generated by Django 5.0 on 2023-12-13 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('essay', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='collegeessay',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]