# Generated by Django 3.1 on 2020-08-26 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auditlog', '0010_auto_20200706_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logentry',
            name='additional_data',
            field=models.JSONField(blank=True, null=True, verbose_name='additional data'),
        ),
        migrations.AlterField(
            model_name='logentry',
            name='changes',
            field=models.JSONField(blank=True, null=True, verbose_name='change message'),
        ),
    ]