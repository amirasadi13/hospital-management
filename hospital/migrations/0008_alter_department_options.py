# Generated by Django 4.1.4 on 2023-05-05 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0007_alter_turncheckeddate_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='department',
            options={'ordering': ['-created_time']},
        ),
    ]
