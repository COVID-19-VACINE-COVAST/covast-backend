# Generated by Django 3.1.5 on 2021-01-17 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='inoculation_at',
            field=models.DateTimeField(null=True),
        ),
    ]
