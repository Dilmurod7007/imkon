# Generated by Django 3.2.9 on 2021-11-13 04:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_alter_sponsor_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sponsor',
            name='my_type',
        ),
    ]
