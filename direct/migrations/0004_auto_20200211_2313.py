# Generated by Django 2.2 on 2020-02-11 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('direct', '0003_auto_20200211_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='code',
            field=models.CharField(blank=True, max_length=7, null=True, unique=True),
        ),
    ]
