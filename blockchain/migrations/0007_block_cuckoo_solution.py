# Generated by Django 2.0 on 2018-07-16 10:01

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blockchain', '0006_block_cuckoo_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='block',
            name='cuckoo_solution',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=[], size=None),
            preserve_default=False,
        ),
    ]
