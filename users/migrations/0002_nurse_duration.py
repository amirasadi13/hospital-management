# Generated by Django 4.1.4 on 2023-05-01 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='nurse',
            name='duration',
            field=models.DurationField(blank=True, null=True),
        ),
    ]