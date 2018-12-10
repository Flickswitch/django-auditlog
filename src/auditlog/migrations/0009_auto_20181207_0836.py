# Generated by Django 2.1.3 on 2018-12-07 14:36

import django.contrib.postgres.indexes
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auditlog', '0008_auto_20181121_0527'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='logentry',
            index=django.contrib.postgres.indexes.GinIndex(fields=['changes'], name='auditlog_lo_changes_9048be_gin'),
        ),
        migrations.AddIndex(
            model_name='logentry',
            index=django.contrib.postgres.indexes.GinIndex(fields=['additional_data'], name='auditlog_lo_additio_87c5bf_gin'),
        ),
    ]
