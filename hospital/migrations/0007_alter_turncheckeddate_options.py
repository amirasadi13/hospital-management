# Generated by Django 4.1.4 on 2023-05-05 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0006_turncheckeddate_checked_time'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='turncheckeddate',
            options={'ordering': ['-created_time']},
        ),
    ]