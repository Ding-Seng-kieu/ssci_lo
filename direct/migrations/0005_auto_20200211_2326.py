# Generated by Django 2.2 on 2020-02-11 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('direct', '0004_auto_20200211_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='coordination',
            field=models.CharField(blank=True, max_length=21, null=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='location',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]