# Generated by Django 4.1.1 on 2022-10-27 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='pro_id',
        ),
    ]
