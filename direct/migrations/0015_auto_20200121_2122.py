# Generated by Django 2.2 on 2020-01-21 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('direct', '0014_remove_heroinfo_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='position',
            name='type_first_choice',
        ),
        migrations.RemoveField(
            model_name='position',
            name='type_second_choice',
        ),
        migrations.AddField(
            model_name='position',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='areainfo', to='direct.AreaInfo'),
        ),
        migrations.AddField(
            model_name='position',
            name='province',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='direct.AreaInfo'),
        ),
        migrations.DeleteModel(
            name='HeroInfo',
        ),
    ]